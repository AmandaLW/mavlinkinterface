# setFluidDensity( density )

This function sets the fluid density (used in depth calculations) to the given value.

Note: changes made by this command persist between dives.

## Parameters

density (int):
> The density in kg/m^3 to set as default.  
> Fresh water is 1000
> Salt water is 1020-1030, depending on salinity  
> Chlorinated pool water is 1000

## Return Values

Returns void

## Examples

```py
MLI.setFluidDensity(1025)
# Sets the fluidDensity value to 1025 kg/m^3
```
