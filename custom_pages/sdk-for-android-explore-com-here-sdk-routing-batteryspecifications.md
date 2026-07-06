---
title: "BatterySpecifications (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-batteryspecifications"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.BatterySpecifications

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">BatterySpecifications</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Parameters related to the electric vehicle's battery.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-field-summary"
  class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
  class="external-link"
  title="class or interface in java.util"><code>Map</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>`>`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#chargingCurve"
  class="member-name-link"><code>chargingCurve</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Function curve describing the maximum battery charging rate (in kW) at
  a given charge level (in kWh).

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#chargingSetupDuration"
  class="member-name-link"><code>chargingSetupDuration</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Time in seconds spent after arriving at a charging station, but before
  actually charging, e.g., time spent for payment processing.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`ChargingConnectorType`](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#connectorTypes"
  class="member-name-link"><code>connectorTypes</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  List of available charging connector types.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#initialChargeInKilowattHours"
  class="member-name-link"><code>initialChargeInKilowattHours</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Charge level of the vehicle's battery at the start of the route (in
  kWh).

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#maxChargingCurrentInAmperes"
  class="member-name-link"><code>maxChargingCurrentInAmperes</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Maximum charging current supported by the vehicle's battery in
  Amperes.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#maxChargingVoltageInVolts"
  class="member-name-link"><code>maxChargingVoltageInVolts</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Maximum charging voltage supported by the vehicle's battery in Volts.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#maxPowerAtLowVoltageInKilowatts"
  class="member-name-link"><code>maxPowerAtLowVoltageInKilowatts</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The maximum power in kilowatts at which a vehicle can charge under
  given these conditions: The charging station connector's maximum
  supply voltage is less than 800 V. maxChargingVoltageInVolts is
  greater than or equal to 800 V.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtChargingStationInKilowattHours"
  class="member-name-link"><code>minChargeAtChargingStationInKilowattHours</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Minimum charge when arriving at a charging station in kWh.

  </div>

  </div>

  <div class="col-first even-row-color">

  `double`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtDestinationInKilowattHours"
  class="member-name-link"><code>minChargeAtDestinationInKilowattHours</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Minimum charge at the final route destination in kWh.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtFirstChargingStationInKilowattHours"
  class="member-name-link"><code>minChargeAtFirstChargingStationInKilowattHours</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Minimum charge when arriving at first charging station in kWh.

  </div>

  </div>

  <div class="col-first even-row-color">

  `double`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours"
  class="member-name-link"><code>targetChargeInKilowattHours</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Maximum charge to which the battery should be charged at a charging
  station (in kWh).

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours"
  class="member-name-link"><code>totalCapacityInKilowattHours</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Total capacity of the vehicle's battery (in kWh).

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      BatterySpecifications()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      BatterySpecifications(double totalCapacityInKilowattHours)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      BatterySpecifications(double totalCapacityInKilowattHours,
       double initialChargeInKilowattHours)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      BatterySpecifications(double totalCapacityInKilowattHours,
       double initialChargeInKilowattHours,
       double targetChargeInKilowattHours)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      BatterySpecifications(double totalCapacityInKilowattHours,
       double initialChargeInKilowattHours,
       double targetChargeInKilowattHours,
       Map<Double,Double> chargingCurve)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      BatterySpecifications(double totalCapacityInKilowattHours,
       double initialChargeInKilowattHours,
       double targetChargeInKilowattHours,
       Map<Double,Double> chargingCurve,
       List<ChargingConnectorType> connectorTypes)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      BatterySpecifications(double totalCapacityInKilowattHours,
       double initialChargeInKilowattHours,
       double targetChargeInKilowattHours,
       Map<Double,Double> chargingCurve,
       List<ChargingConnectorType> connectorTypes,
       double minChargeAtChargingStationInKilowattHours)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      BatterySpecifications(double totalCapacityInKilowattHours,
       double initialChargeInKilowattHours,
       double targetChargeInKilowattHours,
       Map<Double,Double> chargingCurve,
       List<ChargingConnectorType> connectorTypes,
       double minChargeAtChargingStationInKilowattHours,
       Double minChargeAtFirstChargingStationInKilowattHours)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      BatterySpecifications(double totalCapacityInKilowattHours,
       double initialChargeInKilowattHours,
       double targetChargeInKilowattHours,
       Map<Double,Double> chargingCurve,
       List<ChargingConnectorType> connectorTypes,
       double minChargeAtChargingStationInKilowattHours,
       Double minChargeAtFirstChargingStationInKilowattHours,
       double minChargeAtDestinationInKilowattHours)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      BatterySpecifications(double totalCapacityInKilowattHours,
       double initialChargeInKilowattHours,
       double targetChargeInKilowattHours,
       Map<Double,Double> chargingCurve,
       List<ChargingConnectorType> connectorTypes,
       double minChargeAtChargingStationInKilowattHours,
       Double minChargeAtFirstChargingStationInKilowattHours,
       double minChargeAtDestinationInKilowattHours,
       Double maxChargingVoltageInVolts)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      BatterySpecifications(double totalCapacityInKilowattHours,
       double initialChargeInKilowattHours,
       double targetChargeInKilowattHours,
       Map<Double,Double> chargingCurve,
       List<ChargingConnectorType> connectorTypes,
       double minChargeAtChargingStationInKilowattHours,
       Double minChargeAtFirstChargingStationInKilowattHours,
       double minChargeAtDestinationInKilowattHours,
       Double maxChargingVoltageInVolts,
       Double maxChargingCurrentInAmperes)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      BatterySpecifications(double totalCapacityInKilowattHours,
       double initialChargeInKilowattHours,
       double targetChargeInKilowattHours,
       Map<Double,Double> chargingCurve,
       List<ChargingConnectorType> connectorTypes,
       double minChargeAtChargingStationInKilowattHours,
       Double minChargeAtFirstChargingStationInKilowattHours,
       double minChargeAtDestinationInKilowattHours,
       Double maxChargingVoltageInVolts,
       Double maxChargingCurrentInAmperes,
       Duration chargingSetupDuration)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      BatterySpecifications(double totalCapacityInKilowattHours,
       double initialChargeInKilowattHours,
       double targetChargeInKilowattHours,
       Map<Double,Double> chargingCurve,
       List<ChargingConnectorType> connectorTypes,
       double minChargeAtChargingStationInKilowattHours,
       Double minChargeAtFirstChargingStationInKilowattHours,
       double minChargeAtDestinationInKilowattHours,
       Double maxChargingVoltageInVolts,
       Double maxChargingCurrentInAmperes,
       Duration chargingSetupDuration,
       Double maxPowerAtLowVoltageInKilowatts)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals(Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-field-detail"
  class="section field-details">

  - <div id="sdk-for-android-explore-totalCapacityInKilowattHours"
    class="section detail">

    ### totalCapacityInKilowattHours

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">totalCapacityInKilowattHours</span>

    </div>

    <div class="block">

    Total capacity of the vehicle's battery (in kWh). It must be
    positive. Defaults to 0. Note: For a user-planned ChargingStop ,
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an invalid parameter error.

    </div>

    </div>

  - <div id="sdk-for-android-explore-initialChargeInKilowattHours"
    class="section detail">

    ### initialChargeInKilowattHours

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">initialChargeInKilowattHours</span>

    </div>

    <div class="block">

    Charge level of the vehicle's battery at the start of the route (in
    kWh). It must be non-negative and less than or equal to the value of
    totalCapacityInKilowattHours , otherwise the BatterySpecifications
    instance is considered invalid. Defaults to 0. Note: For a
    user-planned ChargingStop , this parameter is also required. If not
    set greater than 0, the route calculation will fail as an an invalid
    parameter error.

    </div>

    </div>

  - <div id="sdk-for-android-explore-targetChargeInKilowattHours"
    class="section detail">

    ### targetChargeInKilowattHours

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">targetChargeInKilowattHours</span>

    </div>

    <div class="block">

    Maximum charge to which the battery should be charged at a charging
    station (in kWh). It must be positive and less than or equal to the
    value of totalCapacityInKilowattHours , otherwise the
    BatterySpecifications instance is considered invalid. Defaults to 0.

    </div>

    </div>

  - <div id="sdk-for-android-explore-chargingCurve"
    class="section detail">

    ### chargingCurve

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>\></span> <span class="element-name">chargingCurve</span>

    </div>

    <div class="block">

    Function curve describing the maximum battery charging rate (in kW)
    at a given charge level (in kWh). Map keys represent charge levels
    that are non-negative floating point values in units of (kWh). Map
    values represent charging rate values that are positive floating
    point values in units of (kW). Given charge levels must cover the
    entire range of \[0, targetChargeInKilowattHours \], otherwise the
    BatterySpecifications instance is considered invalid. The charging
    curve is considered piecewise constant instead of being
    interpolated. Defaults to an empty container. Note: For a
    user-planned ChargingStop , this parameter is also required. If one
    or more values are not set, the route calculation will fail as an
    invalid parameter error.

    </div>

    </div>

  - <div id="sdk-for-android-explore-connectorTypes"
    class="section detail">

    ### connectorTypes

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")\></span> <span class="element-name">connectorTypes</span>

    </div>

    <div class="block">

    List of available charging connector types. It must be at least one
    charging connector type added, otherwise the BatterySpecifications
    instance is considered invalid. Defaults to an empty container.

    </div>

    </div>

  - <div id="sdk-for-android-explore-minChargeAtChargingStationInKilowattHours"
    class="section detail">

    ### minChargeAtChargingStationInKilowattHours

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">minChargeAtChargingStationInKilowattHours</span>

    </div>

    <div class="block">

    Minimum charge when arriving at a charging station in kWh. It must
    be non-negative and less than the value of
    targetChargeInKilowattHours , otherwise the BatterySpecifications
    instance is considered invalid. Defaults to 0.

    </div>

    </div>

  - <div id="sdk-for-android-explore-minChargeAtFirstChargingStationInKilowattHours"
    class="section detail">

    ### minChargeAtFirstChargingStationInKilowattHours

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">minChargeAtFirstChargingStationInKilowattHours</span>

    </div>

    <div class="block">

    Minimum charge when arriving at first charging station in kWh. This
    overrides minChargeAtChargingStationInKilowattHours for the first
    charging station. If not specified,
    minChargeAtChargingStationInKilowattHours will be used for all
    charging stations, including the first one. Defaults to null . When
    initialized, it must be non-negative and less than the value of
    targetChargeInKilowattHours , otherwise the BatterySpecifications
    instance is considered invalid. This is usually used when the
    current charge is too low to reach a charging station within
    minChargeAtChargingStation limits.

    </div>

    </div>

  - <div id="sdk-for-android-explore-minChargeAtDestinationInKilowattHours"
    class="section detail">

    ### minChargeAtDestinationInKilowattHours

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">minChargeAtDestinationInKilowattHours</span>

    </div>

    <div class="block">

    Minimum charge at the final route destination in kWh. It must be
    non-negative and less than the value of targetChargeInKilowattHours
    , otherwise the BatterySpecifications instance is considered
    invalid. Defaults to 0.

    </div>

    </div>

  - <div id="sdk-for-android-explore-maxChargingVoltageInVolts"
    class="section detail">

    ### maxChargingVoltageInVolts

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">maxChargingVoltageInVolts</span>

    </div>

    <div class="block">

    Maximum charging voltage supported by the vehicle's battery in
    Volts. It must be positive. When omitted, the voltage is determined
    by the charging station attributes. Defaults to null .

    </div>

    </div>

  - <div id="sdk-for-android-explore-maxChargingCurrentInAmperes"
    class="section detail">

    ### maxChargingCurrentInAmperes

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">maxChargingCurrentInAmperes</span>

    </div>

    <div class="block">

    Maximum charging current supported by the vehicle's battery in
    Amperes. It must be positive. When omitted, the charging current is
    determined by the charging station attributes. Defaults to null .

    </div>

    </div>

  - <div id="sdk-for-android-explore-chargingSetupDuration"
    class="section detail">

    ### chargingSetupDuration

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">chargingSetupDuration</span>

    </div>

    <div class="block">

    Time in seconds spent after arriving at a charging station, but
    before actually charging, e.g., time spent for payment processing.
    Defaults to 0 seconds.

    </div>

    </div>

  - <div id="sdk-for-android-explore-maxPowerAtLowVoltageInKilowatts"
    class="section detail">

    ### maxPowerAtLowVoltageInKilowatts

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">maxPowerAtLowVoltageInKilowatts</span>

    </div>

    <div class="block">

    The maximum power in kilowatts at which a vehicle can charge under
    given these conditions: The charging station connector's maximum
    supply voltage is less than 800 V. maxChargingVoltageInVolts is
    greater than or equal to 800 V. The provided value must be greater
    than or equal to 0. By default, it is not set. Note: The feature is
    not supported by the OfflineRoutingEngine .

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>()" class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  - <div id="sdk-for-android-explore-<init>(double)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be
    positive. Defaults to 0. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an invalid parameter error.

    </div>

  - <div id="sdk-for-android-explore-<init>(double,double)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be
    positive. Defaults to 0. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in
    kWh). It must be non-negative and less than or equal to the value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0. **Note:** For a
    user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an an invalid parameter error.

    </div>

  - <div id="sdk-for-android-explore-<init>(double,double,double)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be
    positive. Defaults to 0. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in
    kWh). It must be non-negative and less than or equal to the value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0. **Note:** For a
    user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging
    station (in kWh). It must be positive and less than or equal to the
    value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    </div>

  - <div id="sdk-for-android-explore-<init>(double,double,double,java.util.Map)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>\> chargingCurve)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be
    positive. Defaults to 0. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in
    kWh). It must be non-negative and less than or equal to the value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0. **Note:** For a
    user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging
    station (in kWh). It must be positive and less than or equal to the
    value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW)
    at a given charge level (in kWh). Map keys represent charge levels
    that are non-negative floating point values in units of (kWh). Map
    values represent charging rate values that are positive floating
    point values in units of (kW). Given charge levels must cover the
    entire range of \[0,
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours)\],
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. The charging curve is considered
    piecewise constant instead of being interpolated. Defaults to an
    empty container. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If one or more values are not set,
    the route calculation will fail as an invalid parameter error.

    </div>

  - <div id="sdk-for-android-explore-<init>(double,double,double,java.util.Map,java.util.List)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>\> chargingCurve,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")\> connectorTypes)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be
    positive. Defaults to 0. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in
    kWh). It must be non-negative and less than or equal to the value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0. **Note:** For a
    user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging
    station (in kWh). It must be positive and less than or equal to the
    value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW)
    at a given charge level (in kWh). Map keys represent charge levels
    that are non-negative floating point values in units of (kWh). Map
    values represent charging rate values that are positive floating
    point values in units of (kW). Given charge levels must cover the
    entire range of \[0,
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours)\],
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. The charging curve is considered
    piecewise constant instead of being interpolated. Defaults to an
    empty container. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If one or more values are not set,
    the route calculation will fail as an invalid parameter error.

    `connectorTypes` -

    List of available charging connector types. It must be at least one
    charging connector type added, otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to an empty container.

    </div>

  - <div id="sdk-for-android-explore-<init>(double,double,double,java.util.Map,java.util.List,double)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>\> chargingCurve,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")\> connectorTypes,
    double minChargeAtChargingStationInKilowattHours)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be
    positive. Defaults to 0. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in
    kWh). It must be non-negative and less than or equal to the value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0. **Note:** For a
    user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging
    station (in kWh). It must be positive and less than or equal to the
    value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW)
    at a given charge level (in kWh). Map keys represent charge levels
    that are non-negative floating point values in units of (kWh). Map
    values represent charging rate values that are positive floating
    point values in units of (kW). Given charge levels must cover the
    entire range of \[0,
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours)\],
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. The charging curve is considered
    piecewise constant instead of being interpolated. Defaults to an
    empty container. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If one or more values are not set,
    the route calculation will fail as an invalid parameter error.

    `connectorTypes` -

    List of available charging connector types. It must be at least one
    charging connector type added, otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to an empty container.

    `minChargeAtChargingStationInKilowattHours` -

    Minimum charge when arriving at a charging station in kWh. It must
    be non-negative and less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    </div>

  - <div id="sdk-for-android-explore-<init>(double,double,double,java.util.Map,java.util.List,double,java.lang.Double)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>\> chargingCurve,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")\> connectorTypes,
    double minChargeAtChargingStationInKilowattHours, @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be
    positive. Defaults to 0. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in
    kWh). It must be non-negative and less than or equal to the value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0. **Note:** For a
    user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging
    station (in kWh). It must be positive and less than or equal to the
    value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW)
    at a given charge level (in kWh). Map keys represent charge levels
    that are non-negative floating point values in units of (kWh). Map
    values represent charging rate values that are positive floating
    point values in units of (kW). Given charge levels must cover the
    entire range of \[0,
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours)\],
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. The charging curve is considered
    piecewise constant instead of being interpolated. Defaults to an
    empty container. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If one or more values are not set,
    the route calculation will fail as an invalid parameter error.

    `connectorTypes` -

    List of available charging connector types. It must be at least one
    charging connector type added, otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to an empty container.

    `minChargeAtChargingStationInKilowattHours` -

    Minimum charge when arriving at a charging station in kWh. It must
    be non-negative and less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `minChargeAtFirstChargingStationInKilowattHours` -

    Minimum charge when arriving at first charging station in kWh. This
    overrides
    [`minChargeAtChargingStationInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtChargingStationInKilowattHours)
    for the first charging station. If not specified,
    [`minChargeAtChargingStationInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtChargingStationInKilowattHours)
    will be used for all charging stations, including the first one.
    Defaults to `null`. When initialized, it must be non-negative and
    less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. This is usually used when the
    current charge is too low to reach a charging station within
    `minChargeAtChargingStation` limits.

    </div>

  - <div id="sdk-for-android-explore-<init>(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>\> chargingCurve,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")\> connectorTypes,
    double minChargeAtChargingStationInKilowattHours, @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours,
    double minChargeAtDestinationInKilowattHours)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be
    positive. Defaults to 0. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in
    kWh). It must be non-negative and less than or equal to the value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0. **Note:** For a
    user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging
    station (in kWh). It must be positive and less than or equal to the
    value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW)
    at a given charge level (in kWh). Map keys represent charge levels
    that are non-negative floating point values in units of (kWh). Map
    values represent charging rate values that are positive floating
    point values in units of (kW). Given charge levels must cover the
    entire range of \[0,
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours)\],
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. The charging curve is considered
    piecewise constant instead of being interpolated. Defaults to an
    empty container. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If one or more values are not set,
    the route calculation will fail as an invalid parameter error.

    `connectorTypes` -

    List of available charging connector types. It must be at least one
    charging connector type added, otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to an empty container.

    `minChargeAtChargingStationInKilowattHours` -

    Minimum charge when arriving at a charging station in kWh. It must
    be non-negative and less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `minChargeAtFirstChargingStationInKilowattHours` -

    Minimum charge when arriving at first charging station in kWh. This
    overrides
    [`minChargeAtChargingStationInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtChargingStationInKilowattHours)
    for the first charging station. If not specified,
    [`minChargeAtChargingStationInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtChargingStationInKilowattHours)
    will be used for all charging stations, including the first one.
    Defaults to `null`. When initialized, it must be non-negative and
    less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. This is usually used when the
    current charge is too low to reach a charging station within
    `minChargeAtChargingStation` limits.

    `minChargeAtDestinationInKilowattHours` -

    Minimum charge at the final route destination in kWh. It must be
    non-negative and less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    </div>

  - <div id="sdk-for-android-explore-<init>(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>\> chargingCurve,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")\> connectorTypes,
    double minChargeAtChargingStationInKilowattHours, @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours,
    double minChargeAtDestinationInKilowattHours, @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> maxChargingVoltageInVolts)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be
    positive. Defaults to 0. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in
    kWh). It must be non-negative and less than or equal to the value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0. **Note:** For a
    user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging
    station (in kWh). It must be positive and less than or equal to the
    value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW)
    at a given charge level (in kWh). Map keys represent charge levels
    that are non-negative floating point values in units of (kWh). Map
    values represent charging rate values that are positive floating
    point values in units of (kW). Given charge levels must cover the
    entire range of \[0,
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours)\],
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. The charging curve is considered
    piecewise constant instead of being interpolated. Defaults to an
    empty container. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If one or more values are not set,
    the route calculation will fail as an invalid parameter error.

    `connectorTypes` -

    List of available charging connector types. It must be at least one
    charging connector type added, otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to an empty container.

    `minChargeAtChargingStationInKilowattHours` -

    Minimum charge when arriving at a charging station in kWh. It must
    be non-negative and less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `minChargeAtFirstChargingStationInKilowattHours` -

    Minimum charge when arriving at first charging station in kWh. This
    overrides
    [`minChargeAtChargingStationInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtChargingStationInKilowattHours)
    for the first charging station. If not specified,
    [`minChargeAtChargingStationInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtChargingStationInKilowattHours)
    will be used for all charging stations, including the first one.
    Defaults to `null`. When initialized, it must be non-negative and
    less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. This is usually used when the
    current charge is too low to reach a charging station within
    `minChargeAtChargingStation` limits.

    `minChargeAtDestinationInKilowattHours` -

    Minimum charge at the final route destination in kWh. It must be
    non-negative and less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `maxChargingVoltageInVolts` -

    Maximum charging voltage supported by the vehicle's battery in
    Volts. It must be positive. When omitted, the voltage is determined
    by the charging station attributes. Defaults to `null`.

    </div>

  - <div id="sdk-for-android-explore-<init>(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>\> chargingCurve,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")\> connectorTypes,
    double minChargeAtChargingStationInKilowattHours, @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours,
    double minChargeAtDestinationInKilowattHours, @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> maxChargingVoltageInVolts,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> maxChargingCurrentInAmperes)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be
    positive. Defaults to 0. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in
    kWh). It must be non-negative and less than or equal to the value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0. **Note:** For a
    user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging
    station (in kWh). It must be positive and less than or equal to the
    value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW)
    at a given charge level (in kWh). Map keys represent charge levels
    that are non-negative floating point values in units of (kWh). Map
    values represent charging rate values that are positive floating
    point values in units of (kW). Given charge levels must cover the
    entire range of \[0,
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours)\],
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. The charging curve is considered
    piecewise constant instead of being interpolated. Defaults to an
    empty container. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If one or more values are not set,
    the route calculation will fail as an invalid parameter error.

    `connectorTypes` -

    List of available charging connector types. It must be at least one
    charging connector type added, otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to an empty container.

    `minChargeAtChargingStationInKilowattHours` -

    Minimum charge when arriving at a charging station in kWh. It must
    be non-negative and less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `minChargeAtFirstChargingStationInKilowattHours` -

    Minimum charge when arriving at first charging station in kWh. This
    overrides
    [`minChargeAtChargingStationInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtChargingStationInKilowattHours)
    for the first charging station. If not specified,
    [`minChargeAtChargingStationInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtChargingStationInKilowattHours)
    will be used for all charging stations, including the first one.
    Defaults to `null`. When initialized, it must be non-negative and
    less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. This is usually used when the
    current charge is too low to reach a charging station within
    `minChargeAtChargingStation` limits.

    `minChargeAtDestinationInKilowattHours` -

    Minimum charge at the final route destination in kWh. It must be
    non-negative and less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `maxChargingVoltageInVolts` -

    Maximum charging voltage supported by the vehicle's battery in
    Volts. It must be positive. When omitted, the voltage is determined
    by the charging station attributes. Defaults to `null`.

    `maxChargingCurrentInAmperes` -

    Maximum charging current supported by the vehicle's battery in
    Amperes. It must be positive. When omitted, the charging current is
    determined by the charging station attributes. Defaults to `null`.

    </div>

  - <div id="sdk-for-android-explore-<init>(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double,com.here.time.Duration)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>\> chargingCurve,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")\> connectorTypes,
    double minChargeAtChargingStationInKilowattHours, @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours,
    double minChargeAtDestinationInKilowattHours, @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> maxChargingVoltageInVolts,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> maxChargingCurrentInAmperes,
    @NonNull
    [Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time") chargingSetupDuration)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be
    positive. Defaults to 0. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in
    kWh). It must be non-negative and less than or equal to the value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0. **Note:** For a
    user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging
    station (in kWh). It must be positive and less than or equal to the
    value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW)
    at a given charge level (in kWh). Map keys represent charge levels
    that are non-negative floating point values in units of (kWh). Map
    values represent charging rate values that are positive floating
    point values in units of (kW). Given charge levels must cover the
    entire range of \[0,
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours)\],
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. The charging curve is considered
    piecewise constant instead of being interpolated. Defaults to an
    empty container. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If one or more values are not set,
    the route calculation will fail as an invalid parameter error.

    `connectorTypes` -

    List of available charging connector types. It must be at least one
    charging connector type added, otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to an empty container.

    `minChargeAtChargingStationInKilowattHours` -

    Minimum charge when arriving at a charging station in kWh. It must
    be non-negative and less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `minChargeAtFirstChargingStationInKilowattHours` -

    Minimum charge when arriving at first charging station in kWh. This
    overrides
    [`minChargeAtChargingStationInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtChargingStationInKilowattHours)
    for the first charging station. If not specified,
    [`minChargeAtChargingStationInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtChargingStationInKilowattHours)
    will be used for all charging stations, including the first one.
    Defaults to `null`. When initialized, it must be non-negative and
    less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. This is usually used when the
    current charge is too low to reach a charging station within
    `minChargeAtChargingStation` limits.

    `minChargeAtDestinationInKilowattHours` -

    Minimum charge at the final route destination in kWh. It must be
    non-negative and less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `maxChargingVoltageInVolts` -

    Maximum charging voltage supported by the vehicle's battery in
    Volts. It must be positive. When omitted, the voltage is determined
    by the charging station attributes. Defaults to `null`.

    `maxChargingCurrentInAmperes` -

    Maximum charging current supported by the vehicle's battery in
    Amperes. It must be positive. When omitted, the charging current is
    determined by the charging station attributes. Defaults to `null`.

    `chargingSetupDuration` -

    Time in seconds spent after arriving at a charging station, but
    before actually charging, e.g., time spent for payment processing.
    Defaults to 0 seconds.

    </div>

  - <div id="sdk-for-android-explore-<init>(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double,com.here.time.Duration,java.lang.Double)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>\> chargingCurve,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")\> connectorTypes,
    double minChargeAtChargingStationInKilowattHours, @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours,
    double minChargeAtDestinationInKilowattHours, @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> maxChargingVoltageInVolts,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> maxChargingCurrentInAmperes,
    @NonNull
    [Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time") chargingSetupDuration,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> maxPowerAtLowVoltageInKilowatts)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `totalCapacityInKilowattHours` -

    Total capacity of the vehicle's battery (in kWh). It must be
    positive. Defaults to 0. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an invalid parameter error.

    `initialChargeInKilowattHours` -

    Charge level of the vehicle's battery at the start of the route (in
    kWh). It must be non-negative and less than or equal to the value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0. **Note:** For a
    user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If not set greater than 0, the
    route calculation will fail as an an invalid parameter error.

    `targetChargeInKilowattHours` -

    Maximum charge to which the battery should be charged at a charging
    station (in kWh). It must be positive and less than or equal to the
    value of
    [`totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `chargingCurve` -

    Function curve describing the maximum battery charging rate (in kW)
    at a given charge level (in kWh). Map keys represent charge levels
    that are non-negative floating point values in units of (kWh). Map
    values represent charging rate values that are positive floating
    point values in units of (kW). Given charge levels must cover the
    entire range of \[0,
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours)\],
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. The charging curve is considered
    piecewise constant instead of being interpolated. Defaults to an
    empty container. **Note:** For a user-planned
    [`ChargingStop`](sdk-for-android-explore-com-here-sdk-routing-chargingstop "class in com.here.sdk.routing"),
    this parameter is also required. If one or more values are not set,
    the route calculation will fail as an invalid parameter error.

    `connectorTypes` -

    List of available charging connector types. It must be at least one
    charging connector type added, otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to an empty container.

    `minChargeAtChargingStationInKilowattHours` -

    Minimum charge when arriving at a charging station in kWh. It must
    be non-negative and less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `minChargeAtFirstChargingStationInKilowattHours` -

    Minimum charge when arriving at first charging station in kWh. This
    overrides
    [`minChargeAtChargingStationInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtChargingStationInKilowattHours)
    for the first charging station. If not specified,
    [`minChargeAtChargingStationInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtChargingStationInKilowattHours)
    will be used for all charging stations, including the first one.
    Defaults to `null`. When initialized, it must be non-negative and
    less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. This is usually used when the
    current charge is too low to reach a charging station within
    `minChargeAtChargingStation` limits.

    `minChargeAtDestinationInKilowattHours` -

    Minimum charge at the final route destination in kWh. It must be
    non-negative and less than the value of
    [`targetChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours),
    otherwise the
    [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")
    instance is considered invalid. Defaults to 0.

    `maxChargingVoltageInVolts` -

    Maximum charging voltage supported by the vehicle's battery in
    Volts. It must be positive. When omitted, the voltage is determined
    by the charging station attributes. Defaults to `null`.

    `maxChargingCurrentInAmperes` -

    Maximum charging current supported by the vehicle's battery in
    Amperes. It must be positive. When omitted, the charging current is
    determined by the charging station attributes. Defaults to `null`.

    `chargingSetupDuration` -

    Time in seconds spent after arriving at a charging station, but
    before actually charging, e.g., time spent for payment processing.
    Defaults to 0 seconds.

    `maxPowerAtLowVoltageInKilowatts` -

    The maximum power in kilowatts at which a vehicle can charge under
    given these conditions:

    - The charging station connector's maximum supply voltage is less
      than 800 V.
    - [`maxChargingVoltageInVolts`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#maxChargingVoltageInVolts)
      is greater than or equal to 800 V. The provided value must be
      greater than or equal to 0. By default, it is not set. **Note:**
      The feature is not supported by the `OfflineRoutingEngine`.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-equals(java.lang.Object)"
    class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
    class="external-link"
    title="class or interface in java.lang"><code>equals</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode()" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
    class="external-link"
    title="class or interface in java.lang"><code>hashCode</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

</div>

