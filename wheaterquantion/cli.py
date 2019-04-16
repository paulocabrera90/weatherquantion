# -*- coding: utf-8 -*-
"""
Este módulo es el punto de entrada __main__ para la útilidad de comando.
"""
import datetime
import enum
import click


from wheaterquantion.core.wheater.job.watcher import WeatherWatcher
from wheaterquantion.core.wheater.statistics import coroutine as coro
from wheaterquantion.core.wheater.statistics.coroutine import WheaterStatsSumary
from wheaterquantion.core.galaxy.simulator import SpaceTime


NOW = datetime.datetime.now()

ONE_HUMAN_YEAR = 365
ONE_VULCAN_YEAR = 72
ONE_BETASOIDE_YEAR = 120
ONE_FERENGI_YEAR = 360


def generate_entropy():
    click.clear()
    click.echo('__          ___                _             ____                    _   _')               
    click.echo('\ \        / / |              | |           / __ \                  | | (_)') 
    click.echo(' \ \  /\  / /| |__   ___  __ _| |_ ___ _ __| |  | |_   _  __ _ _ __ | |_ _  ___  _ __')  
    click.echo("  \ \/  \/ / | '_ \ / _ \/ _` | __/ _ \ '__| |  | | | | |/ _` | '_ \| __| |/ _ \| '_ \ ")  
    click.echo("   \  /\  /  | | | |  __/ (_| | ||  __/ |  | |__| | |_| | (_| | | | | |_| | (_) | | | |")  
    click.echo("    \/  \/   |_| |_|\___|\__,_|\__\___|_|   \___\_\\__,_|\__,_|_| |_|\__|_|\___/|_| |_|")  
    

class CommandLineOption(enum.IntEnum):
    """Lista de opciones de la app, línea de comandos.
    """
    FORECASTING = 1
    INIT_WHEATER_JOB = 2


@click.option('--generardatos', default=365*10)

   

def main():
    generate_entropy()

    opts = {
        CommandLineOption.FORECASTING: 'Pronóstico de Clima por Años. (simulación)',
       
    }
  
    for opcion, descripcion in opts.items():
        click.echo('[{:d}] {:s}.'.format(opcion, descripcion))
    # mostrar opciones
    show_options()


@click.command()
@click.option('--option', default=1, prompt='Seleccione una opción:')
def show_options(option):
    """Listado de opciones diponibles.
    """
    if option == CommandLineOption.FORECASTING:
        forecast_wheater()
    else:
        click.echo('Debes seleccionar una opción')


@click.command()
@click.option('--years', default=10, prompt='Indique el número de años a predecir. Default (10):')
def forecast_wheater(years):

    days_to_calculate = 365 * years

    # llamammos subrutina, indicandole cuántos registros procesar antes de su cierre "automático".
    coro_stats = coro.listen_stream(days_to_calculate)

    try:

        click.echo('preparando simulación de {} años. {} días...'.format(years, days_to_calculate))

        # iniciamos "simulación" planetaria...partiendo del día Cero.
        data_space_stream = SpaceTime.galaxy(from_day=0, to_day=days_to_calculate)

        with click.progressbar(data_space_stream, length=days_to_calculate) as stream:

            for data in stream:
                # envíamos el (día, el clima, y el nivel de precipitación) para estadísticas.
                coro_stats.send(
                    (data.day, data.wheater, data.precipitation)
                )

    except StopIteration as result:

        if isinstance(result.value, WheaterStatsSumary):

            # predicciones y datos estadísticos después de la "simulación"
            forecasting = result.value
            click.echo('*' * 100)

            # mostramos pronóstico del tiempo...
            click.echo(forecasting.periods_summary)
            click.echo(forecasting.pluviometer.summary)
            click.echo(forecasting.general_stats)
        else:
            raise

if __name__ == "__main__":
    main()
