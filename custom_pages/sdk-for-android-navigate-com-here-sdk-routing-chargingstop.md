---
title: "ChargingStop (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-chargingstop"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-routing-package-summary">com.here.sdk.routing</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.ChargingStop → com.here.sdk.routing.ChargingStop

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">ChargingStop</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

The options to specify a user-planned charging stop. Note: In order to specify this ChargingStop , it is also required to set \[sdk.routing.BatterySpecifications.total_capacity_in_kilowatt_hours\], \[sdk.routing.BatterySpecifications.initial_charge_in_kilowatt_hours\], and \[sdk.routing.BatterySpecifications.charging_curve\]. Without all of them, the route calculation will fail as an invalid parameter error.

</div>

</div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

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

  `double`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-chargingstop#currentInAmperes" class="member-name-link"><code>currentInAmperes</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The value of rated current of the connector (in A).

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">`Duration`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-chargingstop#maxDuration" class="member-name-link"><code>maxDuration</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The maximum duration the user plans to charge at the station, including BatterySpecifications.chargingSetupDuration .

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">`Duration`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-chargingstop#minDuration" class="member-name-link"><code>minDuration</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The minimum duration the user expects to charge at the station, including BatterySpecifications.chargingSetupDuration .

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-chargingstop#powerInKilowatts" class="member-name-link"><code>powerInKilowatts</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The value of rated power of the connector (in kW).

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-chargingsupplytype" title="enum class in com.here.sdk.routing">`ChargingSupplyType`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-chargingstop#supplyType" class="member-name-link"><code>supplyType</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Supply type of the suggested connector.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-chargingstop#voltageInVolts" class="member-name-link"><code>voltageInVolts</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The value of rated voltage of the connector (in V).

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

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

      ChargingStop ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      ChargingStop (double powerInKilowatts,
       double currentInAmperes,
       double voltageInVolts, ChargingSupplyType supplyType, Duration minDuration, Duration maxDuration)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

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

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-powerInKilowatts" class="section detail">

    ### powerInKilowatts

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">powerInKilowatts</span>

    </div>

    <div class="block">

    The value of rated power of the connector (in kW).

    </div>

    </div>

  - <div id="sdk-for-android-navigate-currentInAmperes" class="section detail">

    ### currentInAmperes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">currentInAmperes</span>

    </div>

    <div class="block">

    The value of rated current of the connector (in A).

    </div>

    </div>

  - <div id="sdk-for-android-navigate-voltageInVolts" class="section detail">

    ### voltageInVolts

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">voltageInVolts</span>

    </div>

    <div class="block">

    The value of rated voltage of the connector (in V).

    </div>

    </div>

  - <div id="sdk-for-android-navigate-supplyType" class="section detail">

    ### supplyType

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-chargingsupplytype" title="enum class in com.here.sdk.routing">ChargingSupplyType</a></span> <span class="element-name">supplyType</span>

    </div>

    <div class="block">

    Supply type of the suggested connector.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-minDuration" class="section detail">

    ### minDuration

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">minDuration</span>

    </div>

    <div class="block">

    The minimum duration the user expects to charge at the station, including BatterySpecifications.chargingSetupDuration . Note: At least one of min_duration and max_duration is required for a user-planned charging stop. For most use cases, providing at least min_duration is recommended.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-maxDuration" class="section detail">

    ### maxDuration

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">maxDuration</span>

    </div>

    <div class="block">

    The maximum duration the user plans to charge at the station, including BatterySpecifications.chargingSetupDuration . Note: At least one of min_duration and max_duration is required for a user-planned charging stop. For most use cases, providing at least min_duration is recommended.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### ChargingStop

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ChargingStop</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-init-double-double-double-com-here-sdk-routing-ChargingSupplyType-com-here-time-Duration-com-here-time-Duration" class="section detail">

    ### ChargingStop

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ChargingStop</span><wbr></wbr><span class="parameters">(double powerInKilowatts, double currentInAmperes, double voltageInVolts, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-routing-chargingsupplytype" title="enum class in com.here.sdk.routing">ChargingSupplyType</a> supplyType, @Nullable <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> minDuration, @Nullable <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> maxDuration)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `powerInKilowatts` -

    The value of rated power of the connector (in kW).

    `currentInAmperes` -

    The value of rated current of the connector (in A).

    `voltageInVolts` -

    The value of rated voltage of the connector (in V).

    `supplyType` -

    Supply type of the suggested connector.

    `minDuration` -

    The minimum duration the user expects to charge at the station, including <a href="sdk-for-android-navigate-com-here-sdk-routing-batteryspecifications#chargingSetupDuration">`BatterySpecifications.chargingSetupDuration`</a>. **Note:** At least one of `min_duration` and `max_duration` is required for a user-planned charging stop. For most use cases, providing at least `min_duration` is recommended.

    `maxDuration` -

    The maximum duration the user plans to charge at the station, including <a href="sdk-for-android-navigate-com-here-sdk-routing-batteryspecifications#chargingSetupDuration">`BatterySpecifications.chargingSetupDuration`</a>. **Note:** At least one of `min_duration` and `max_duration` is required for a user-planned charging stop. For most use cases, providing at least `min_duration` is recommended.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-navigate-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

