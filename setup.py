from cx_Freeze import setup, Executable
setup(name = "Daily-fuel-price",
      version = "2.1",
      description = "Daily fuel prices across all metros.",
      executables = [Executable("daily-fuel-prices.py")]
      )
