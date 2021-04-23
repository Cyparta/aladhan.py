import asyncio

from aladhan import (
    AsyncClient, TimingsDateArg, DefaultArgs, methods, Tune,
    Schools, MidnightModes, LatitudeAdjustmentMethods, Data
)


async def main():
    client = AsyncClient()
    # getting a Data obj of the response
    data: Data = await client.get_timings(longitude=69, latitude=42)
    # or even specify more
    data: Data = await client.get_timings(
        longitude=69,
        latitude=42,
        date=TimingsDateArg(
            "23-04-2021"  # it also accepts an int (unix time) and datetime() obj
        ),
        defaults=DefaultArgs(
            method=methods.ISNA,  # methods.all_methods to see all available methods
            tune=Tune(
                Asr=+10,
                # and other params ...
            ),
            school=Schools.SHAFI,
            midnightMode=MidnightModes.JAFARI,
            latitudeAdjustmentMethod=LatitudeAdjustmentMethods.ANGLE_BASED,
            adjustment=1
        )
    )
    # or you can get it using address
    data: Data = await client.get_timings_by_address(address="London")

    # or using city
    data: Data = await client.get_timings_by_city(
        country="United Kingdom",
        city="London"
    )

    timings = data.timings
    for k, v in timings.prayers_only.items():
        print(f"{k} at {v.time}, {v.remaining()} left")


asyncio.run(main())
