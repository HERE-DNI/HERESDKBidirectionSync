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

<div id="class-description" class="section class-description">

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

- <div id="field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Field</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
  class="external-link"
  title="class or interface in java.util"><code>Map</code></a><code>&lt;</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a><code>,</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#chargingCurve"
  class="member-name-link"><code>chargingCurve</code></a></td>
  <td><div class="block">
  Function curve describing the maximum battery charging rate (in kW) at a
  given charge level (in kWh).
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-time-duration"
  title="class in com.here.time"><code>Duration</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#chargingSetupDuration"
  class="member-name-link"><code>chargingSetupDuration</code></a></td>
  <td><div class="block">
  Time in seconds spent after arriving at a charging station, but before
  actually charging, e.g., time spent for payment processing.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype"
  title="enum class in com.here.sdk.routing"><code>ChargingConnectorType</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#connectorTypes"
  class="member-name-link"><code>connectorTypes</code></a></td>
  <td><div class="block">
  List of available charging connector types.
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#initialChargeInKilowattHours"
  class="member-name-link"><code>initialChargeInKilowattHours</code></a></td>
  <td><div class="block">
  Charge level of the vehicle's battery at the start of the route (in
  kWh).
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#maxChargingCurrentInAmperes"
  class="member-name-link"><code>maxChargingCurrentInAmperes</code></a></td>
  <td><div class="block">
  Maximum charging current supported by the vehicle's battery in Amperes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#maxChargingVoltageInVolts"
  class="member-name-link"><code>maxChargingVoltageInVolts</code></a></td>
  <td><div class="block">
  Maximum charging voltage supported by the vehicle's battery in Volts.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#maxPowerAtLowVoltageInKilowatts"
  class="member-name-link"><code>maxPowerAtLowVoltageInKilowatts</code></a></td>
  <td><div class="block">
  The maximum power in kilowatts at which a vehicle can charge under given
  these conditions: The charging station connector's maximum supply
  voltage is less than 800 V. maxChargingVoltageInVolts is greater than or
  equal to 800 V.
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtChargingStationInKilowattHours"
  class="member-name-link"><code>minChargeAtChargingStationInKilowattHours</code></a></td>
  <td><div class="block">
  Minimum charge when arriving at a charging station in kWh.
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtDestinationInKilowattHours"
  class="member-name-link"><code>minChargeAtDestinationInKilowattHours</code></a></td>
  <td><div class="block">
  Minimum charge at the final route destination in kWh.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#minChargeAtFirstChargingStationInKilowattHours"
  class="member-name-link"><code>minChargeAtFirstChargingStationInKilowattHours</code></a></td>
  <td><div class="block">
  Minimum charge when arriving at first charging station in kWh.
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#targetChargeInKilowattHours"
  class="member-name-link"><code>targetChargeInKilowattHours</code></a></td>
  <td><div class="block">
  Maximum charge to which the battery should be charged at a charging
  station (in kWh).
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours"
  class="member-name-link"><code>totalCapacityInKilowattHours</code></a></td>
  <td><div class="block">
  Total capacity of the vehicle's battery (in kWh).
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Constructor</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><pre><code>BatterySpecifications()</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>BatterySpecifications(double totalCapacityInKilowattHours)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>BatterySpecifications(double totalCapacityInKilowattHours,
   double initialChargeInKilowattHours)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>BatterySpecifications(double totalCapacityInKilowattHours,
   double initialChargeInKilowattHours,
   double targetChargeInKilowattHours)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>BatterySpecifications(double totalCapacityInKilowattHours,
   double initialChargeInKilowattHours,
   double targetChargeInKilowattHours,
   Map&lt;Double,Double&gt; chargingCurve)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>BatterySpecifications(double totalCapacityInKilowattHours,
   double initialChargeInKilowattHours,
   double targetChargeInKilowattHours,
   Map&lt;Double,Double&gt; chargingCurve,
   List&lt;ChargingConnectorType&gt; connectorTypes)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>BatterySpecifications(double totalCapacityInKilowattHours,
   double initialChargeInKilowattHours,
   double targetChargeInKilowattHours,
   Map&lt;Double,Double&gt; chargingCurve,
   List&lt;ChargingConnectorType&gt; connectorTypes,
   double minChargeAtChargingStationInKilowattHours)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>BatterySpecifications(double totalCapacityInKilowattHours,
   double initialChargeInKilowattHours,
   double targetChargeInKilowattHours,
   Map&lt;Double,Double&gt; chargingCurve,
   List&lt;ChargingConnectorType&gt; connectorTypes,
   double minChargeAtChargingStationInKilowattHours,
   Double minChargeAtFirstChargingStationInKilowattHours)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>BatterySpecifications(double totalCapacityInKilowattHours,
   double initialChargeInKilowattHours,
   double targetChargeInKilowattHours,
   Map&lt;Double,Double&gt; chargingCurve,
   List&lt;ChargingConnectorType&gt; connectorTypes,
   double minChargeAtChargingStationInKilowattHours,
   Double minChargeAtFirstChargingStationInKilowattHours,
   double minChargeAtDestinationInKilowattHours)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>BatterySpecifications(double totalCapacityInKilowattHours,
   double initialChargeInKilowattHours,
   double targetChargeInKilowattHours,
   Map&lt;Double,Double&gt; chargingCurve,
   List&lt;ChargingConnectorType&gt; connectorTypes,
   double minChargeAtChargingStationInKilowattHours,
   Double minChargeAtFirstChargingStationInKilowattHours,
   double minChargeAtDestinationInKilowattHours,
   Double maxChargingVoltageInVolts)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>BatterySpecifications(double totalCapacityInKilowattHours,
   double initialChargeInKilowattHours,
   double targetChargeInKilowattHours,
   Map&lt;Double,Double&gt; chargingCurve,
   List&lt;ChargingConnectorType&gt; connectorTypes,
   double minChargeAtChargingStationInKilowattHours,
   Double minChargeAtFirstChargingStationInKilowattHours,
   double minChargeAtDestinationInKilowattHours,
   Double maxChargingVoltageInVolts,
   Double maxChargingCurrentInAmperes)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>BatterySpecifications(double totalCapacityInKilowattHours,
   double initialChargeInKilowattHours,
   double targetChargeInKilowattHours,
   Map&lt;Double,Double&gt; chargingCurve,
   List&lt;ChargingConnectorType&gt; connectorTypes,
   double minChargeAtChargingStationInKilowattHours,
   Double minChargeAtFirstChargingStationInKilowattHours,
   double minChargeAtDestinationInKilowattHours,
   Double maxChargingVoltageInVolts,
   Double maxChargingCurrentInAmperes,
   Duration chargingSetupDuration)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>BatterySpecifications(double totalCapacityInKilowattHours,
   double initialChargeInKilowattHours,
   double targetChargeInKilowattHours,
   Map&lt;Double,Double&gt; chargingCurve,
   List&lt;ChargingConnectorType&gt; connectorTypes,
   double minChargeAtChargingStationInKilowattHours,
   Double minChargeAtFirstChargingStationInKilowattHours,
   double minChargeAtDestinationInKilowattHours,
   Double maxChargingVoltageInVolts,
   Double maxChargingCurrentInAmperes,
   Duration chargingSetupDuration,
   Double maxPowerAtLowVoltageInKilowatts)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>equals(Object obj)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
  <td> </td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="field-detail" class="section field-details">

  - <div id="totalCapacityInKilowattHours" class="section detail">

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

  - <div id="initialChargeInKilowattHours" class="section detail">

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

  - <div id="targetChargeInKilowattHours" class="section detail">

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

  - <div id="chargingCurve" class="section detail">

    ### chargingCurve

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>></span> <span class="element-name">chargingCurve</span>

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

  - <div id="connectorTypes" class="section detail">

    ### connectorTypes

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")></span> <span class="element-name">connectorTypes</span>

    </div>

    <div class="block">

    List of available charging connector types. It must be at least one
    charging connector type added, otherwise the BatterySpecifications
    instance is considered invalid. Defaults to an empty container.

    </div>

    </div>

  - <div id="minChargeAtChargingStationInKilowattHours"
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

  - <div id="minChargeAtFirstChargingStationInKilowattHours"
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

  - <div id="minChargeAtDestinationInKilowattHours"
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

  - <div id="maxChargingVoltageInVolts" class="section detail">

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

  - <div id="maxChargingCurrentInAmperes" class="section detail">

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

  - <div id="chargingSetupDuration" class="section detail">

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

  - <div id="maxPowerAtLowVoltageInKilowatts" class="section detail">

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

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  - <div id="<init>(double)" class="section detail">

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

  - <div id="<init>(double,double)" class="section detail">

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

  - <div id="<init>(double,double,double)" class="section detail">

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

  - <div id="<init>(double,double,double,java.util.Map)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>> chargingCurve)</span>

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

  - <div id="<init>(double,double,double,java.util.Map,java.util.List)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>> chargingCurve,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")> connectorTypes)</span>

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

  - <div id="<init>(double,double,double,java.util.Map,java.util.List,double)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>> chargingCurve,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")> connectorTypes,
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

  - <div id="<init>(double,double,double,java.util.Map,java.util.List,double,java.lang.Double)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>> chargingCurve,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")> connectorTypes,
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

  - <div id="<init>(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>> chargingCurve,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")> connectorTypes,
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

  - <div id="<init>(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>> chargingCurve,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")> connectorTypes,
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

  - <div id="<init>(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>> chargingCurve,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")> connectorTypes,
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

  - <div id="<init>(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double,com.here.time.Duration)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>> chargingCurve,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")> connectorTypes,
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

  - <div id="<init>(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double,com.here.time.Duration,java.lang.Double)"
    class="section detail">

    ### BatterySpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><span class="parameters">(double totalCapacityInKilowattHours,
    double initialChargeInKilowattHours,
    double targetChargeInKilowattHours, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>> chargingCurve,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")> connectorTypes,
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

- <div id="method-detail" class="section method-details">

  - <div id="equals(java.lang.Object)" class="section detail">

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

  - <div id="hashCode()" class="section detail">

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

