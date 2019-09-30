# Cashflows

The cashflows-application facilitates the financial analysis of investment projects given a csv-file containing the cashflow configuration. 


## Usage

Two main option:

* `describe_investment`: Provides basic financial information given the cashflow config.
* `plot_investment`: Plots the cashflows; x=t y=amount.

### Describe Investment

The `describe_investment` command runs as: 

```commandline
$ python main.py describe_investment --filepath data/cashflows-1.csv --hurdle-rate 0.08
```

Options: 

```text
    --filepath      : Path to csv-file with cashflows. Columns: amount, t
    --hurdle-rate   : Numeric value representing the hurdle rate.
                      * Default: None
```

Examples: 

```commandline
$ python main.py describe_investment --filepath data/cashflows-1.csv                   
  {
      "irr": 0.2205891139852516,
      "hurdle-rate": 0.08,
      "net-present-value": 653.7191648116468,
      "equivalent-annuity": 163.72818430111846
  }
```

```commandline
$ python main.py describe_investment --filepath data/cashflows-2.csv --hurdle-rate 0.02
{
    "irr": 0.059817182267134505,
    "hurdle-rate": 0.02,
    "net-present-value": 12.727618883755255,
    "equivalent-annuity": 3.3425750338217486
}
```

### Plot investment

The `plot_investment` command runs as: 

```commandline
python main.py plot_investment --filepath data/cashflows-1.csv  --save file.png --show
```

Options: 

```text
    --filepath  : Path to csv-file with cashflows. Columns: amount, t
    --save      : String that represents a filename to save the visualization. Empty strings are ignored.
                  * Default: ""
    --show      : Flag that represents weather to show or not the plot. 
```

Examples: 

```commandline
$ python main.py plot_investment --filepath data/cashflows-1.csv  --save file-1.png 
```

```commandline
$ python main.py plot_investment --filepath data/cashflows-2.csv  --show 
```