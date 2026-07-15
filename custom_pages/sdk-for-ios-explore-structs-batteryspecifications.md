---
title: "BatterySpecifications Structure Reference"
slug: "sdk-for-ios-explore-structs-batteryspecifications"
---

# BatterySpecifications

<div class="declaration">

<div class="language">

``` highlight
public struct BatterySpecifications : Hashable
```

</div>

</div>

Parameters related to the electric vehicle’s battery.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk21BatterySpecificationsV28totalCapacityInKilowattHoursSdvp"></span>` `<span id="//apple_ref/swift/Property/totalCapacityInKilowattHours" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV28totalCapacityInKilowattHoursSdvp" class="token"><code>totalCapacityInKilowattHours</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Total capacity of the vehicle’s battery (in kWh). It must be positive. Defaults to 0. **Note:** For a user-planned <a href="sdk-for-ios-explore-structs-chargingstop">`ChargingStop`</a>, this parameter is also required. If not set greater than 0, the route calculation will fail as an invalid parameter error.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var totalCapacityInKilowattHours: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21BatterySpecificationsV28initialChargeInKilowattHoursSdvp"></span>` `<span id="//apple_ref/swift/Property/initialChargeInKilowattHours" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV28initialChargeInKilowattHoursSdvp" class="token"><code>initialChargeInKilowattHours</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Charge level of the vehicle’s battery at the start of the route (in kWh). It must be non-negative and less than or equal to the value of <a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV28totalCapacityInKilowattHoursSdvp">`BatterySpecifications.totalCapacityInKilowattHours`</a>, otherwise the `BatterySpecifications` instance is considered invalid. Defaults to 0. **Note:** For a user-planned <a href="sdk-for-ios-explore-structs-chargingstop">`ChargingStop`</a>, this parameter is also required. If not set greater than 0, the route calculation will fail as an an invalid parameter error.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var initialChargeInKilowattHours: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21BatterySpecificationsV27targetChargeInKilowattHoursSdvp"></span>` `<span id="//apple_ref/swift/Property/targetChargeInKilowattHours" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV27targetChargeInKilowattHoursSdvp" class="token"><code>targetChargeInKilowattHours</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maximum charge to which the battery should be charged at a charging station (in kWh). It must be positive and less than or equal to the value of <a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV28totalCapacityInKilowattHoursSdvp">`BatterySpecifications.totalCapacityInKilowattHours`</a>, otherwise the `BatterySpecifications` instance is considered invalid. Defaults to 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var targetChargeInKilowattHours: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21BatterySpecificationsV13chargingCurveSDyS2dGvp"></span>` `<span id="//apple_ref/swift/Property/chargingCurve" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV13chargingCurveSDyS2dGvp" class="token"><code>chargingCurve</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Function curve describing the maximum battery charging rate (in kW) at a given charge level (in kWh). Map keys represent charge levels that are non-negative floating point values in units of (kWh). Map values represent charging rate values that are positive floating point values in units of (kW). Given charge levels must cover the entire range of \<a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV27targetChargeInKilowattHoursSdvp">0, [`BatterySpecifications.targetChargeInKilowattHours`</a>\], otherwise the `BatterySpecifications` instance is considered invalid. The charging curve is considered piecewise constant instead of being interpolated. Defaults to an empty container. **Note:** For a user-planned <a href="sdk-for-ios-explore-structs-chargingstop">`ChargingStop`</a>, this parameter is also required. If one or more values are not set, the route calculation will fail as an invalid parameter error.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var chargingCurve: [Double : Double]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21BatterySpecificationsV14connectorTypesSayAA21ChargingConnectorTypeOGvp"></span>` `<span id="//apple_ref/swift/Property/connectorTypes" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV14connectorTypesSayAA21ChargingConnectorTypeOGvp" class="token"><code>connectorTypes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of available charging connector types. It must be at least one charging connector type added, otherwise the `BatterySpecifications` instance is considered invalid. Defaults to an empty container.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var connectorTypes: [ChargingConnectorType]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21BatterySpecificationsV41minChargeAtChargingStationInKilowattHoursSdvp"></span>` `<span id="//apple_ref/swift/Property/minChargeAtChargingStationInKilowattHours" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV41minChargeAtChargingStationInKilowattHoursSdvp" class="token"><code>minChargeAtChargingStationInKilowattHours</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Minimum charge when arriving at a charging station in kWh. It must be non-negative and less than the value of <a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV27targetChargeInKilowattHoursSdvp">`BatterySpecifications.targetChargeInKilowattHours`</a>, otherwise the `BatterySpecifications` instance is considered invalid. Defaults to 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var minChargeAtChargingStationInKilowattHours: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21BatterySpecificationsV46minChargeAtFirstChargingStationInKilowattHoursSdSgvp"></span>` `<span id="//apple_ref/swift/Property/minChargeAtFirstChargingStationInKilowattHours" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV46minChargeAtFirstChargingStationInKilowattHoursSdSgvp" class="token"><code>minChargeAtFirstChargingStationInKilowattHours</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Minimum charge when arriving at first charging station in kWh. This overrides <a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV41minChargeAtChargingStationInKilowattHoursSdvp">`BatterySpecifications.minChargeAtChargingStationInKilowattHours`</a> for the first charging station. If not specified, <a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV41minChargeAtChargingStationInKilowattHoursSdvp">`BatterySpecifications.minChargeAtChargingStationInKilowattHours`</a> will be used for all charging stations, including the first one. Defaults to `nil`. When initialized, it must be non-negative and less than the value of <a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV27targetChargeInKilowattHoursSdvp">`BatterySpecifications.targetChargeInKilowattHours`</a>, otherwise the `BatterySpecifications` instance is considered invalid. This is usually used when the current charge is too low to reach a charging station within `minChargeAtChargingStation` limits.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var minChargeAtFirstChargingStationInKilowattHours: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21BatterySpecificationsV37minChargeAtDestinationInKilowattHoursSdvp"></span>` `<span id="//apple_ref/swift/Property/minChargeAtDestinationInKilowattHours" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV37minChargeAtDestinationInKilowattHoursSdvp" class="token"><code>minChargeAtDestinationInKilowattHours</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Minimum charge at the final route destination in kWh. It must be non-negative and less than the value of <a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV27targetChargeInKilowattHoursSdvp">`BatterySpecifications.targetChargeInKilowattHours`</a>, otherwise the `BatterySpecifications` instance is considered invalid. Defaults to 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var minChargeAtDestinationInKilowattHours: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21BatterySpecificationsV25maxChargingVoltageInVoltsSdSgvp"></span>` `<span id="//apple_ref/swift/Property/maxChargingVoltageInVolts" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV25maxChargingVoltageInVoltsSdSgvp" class="token"><code>maxChargingVoltageInVolts</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maximum charging voltage supported by the vehicle’s battery in Volts. It must be positive. When omitted, the voltage is determined by the charging station attributes. Defaults to `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxChargingVoltageInVolts: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21BatterySpecificationsV27maxChargingCurrentInAmperesSdSgvp"></span>` `<span id="//apple_ref/swift/Property/maxChargingCurrentInAmperes" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV27maxChargingCurrentInAmperesSdSgvp" class="token"><code>maxChargingCurrentInAmperes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maximum charging current supported by the vehicle’s battery in Amperes. It must be positive. When omitted, the charging current is determined by the charging station attributes. Defaults to `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxChargingCurrentInAmperes: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21BatterySpecificationsV21chargingSetupDurationSdvp"></span>` `<span id="//apple_ref/swift/Property/chargingSetupDuration" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV21chargingSetupDurationSdvp" class="token"><code>chargingSetupDuration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Time in seconds spent after arriving at a charging station, but before actually charging, e.g., time spent for payment processing. Defaults to 0 seconds.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var chargingSetupDuration: TimeInterval
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21BatterySpecificationsV31maxPowerAtLowVoltageInKilowattsSdSgvp"></span>` `<span id="//apple_ref/swift/Property/maxPowerAtLowVoltageInKilowatts" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV31maxPowerAtLowVoltageInKilowattsSdSgvp" class="token"><code>maxPowerAtLowVoltageInKilowatts</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The maximum power in kilowatts at which a vehicle can charge under given these conditions:

  - The charging station connector’s maximum supply voltage is less than 800 V.
  - <a href="sdk-for-ios-explore-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV25maxChargingVoltageInVoltsSdSgvp">`BatterySpecifications.maxChargingVoltageInVolts`</a> is greater than or equal to 800 V. The provided value must be greater than or equal to 0. By default, it is not set. **Note:** The feature is not supported by the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxPowerAtLowVoltageInKilowatts: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(totalCapacityInKilowattHours: initialChargeInKilowattHours: targetChargeInKilowattHours: chargingCurve: connectorTypes: minChargeAtChargingStationInKilowattHours: minChargeAtFirstChargingStationInKilowattHours: minChargeAtDestinationInKilowattHours: maxChargingVoltageInVolts: maxChargingCurrentInAmperes: chargingSetupDuration: maxPowerAtLowVoltageInKilowatts: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( totalCapacityInKilowattHours : Double = 0.0 , initialChargeInKilowattHours : Double = 0.0 , targetChargeInKilowattHours : Double = 0.0 , chargingCurve : [ Double : Double ] = [:], connectorTypes : [ ChargingConnectorType ] = [], minChargeAtChargingStationInKilowattHours : Double = 0.0 , minChargeAtFirstChargingStationInKilowattHours : Double ? = nil , minChargeAtDestinationInKilowattHours : Double = 0.0 , maxChargingVoltageInVolts : Double ? = nil , maxChargingCurrentInAmperes : Double ? = nil , chargingSetupDuration : TimeInterval = 0 , maxPowerAtLowVoltageInKilowatts : Double ? = nil )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

