---
title: "EmpiricalConsumptionModel (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-empiricalconsumptionmodel"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-routing-package-summary">com.here.sdk.routing</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.EmpiricalConsumptionModel → com.here.sdk.routing.EmpiricalConsumptionModel

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">EmpiricalConsumptionModel</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

This model defines a data-driven energy consumption model for electric vehicles. It estimates the electrical energy required to traverse a route by combining empirically derived vehicle parameters with route characteristics such as distance, elevation changes, and driving speed. Rather than relying on a full physical simulation, this model uses observed consumption behavior to produce realistic and efficient energy estimates suitable for routing, range prediction, and navigation use cases. Parameters specific to the electric vehicle are used to calculate energy consumption on a given route. At minimum, you must provide ascentConsumptionInWattHoursPerMeter , descentRecoveryInWattHoursPerMeter and a freeFlowSpeedTable . Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

  <a href="sdk-for-android-navigate-com-here-sdk-routing-empiricalconsumptionmodel#ascentConsumptionInWattHoursPerMeter" class="member-name-link"><code>ascentConsumptionInWattHoursPerMeter</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Rate of energy consumed per meter rise in elevation (in Wh/m, i.e., Watt-hours per meter).

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-empiricalconsumptionmodel#auxiliaryConsumptionInWattHoursPerSecond" class="member-name-link"><code>auxiliaryConsumptionInWattHoursPerSecond</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Rate of energy (in Wh/s) consumed by the vehicle's auxiliary systems (e.g., air conditioning, lights) per second of travel.

  </div>

  </div>

  <div class="col-first even-row-color">

  `double`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-empiricalconsumptionmodel#descentRecoveryInWattHoursPerMeter" class="member-name-link"><code>descentRecoveryInWattHoursPerMeter</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Rate of energy recovered per meter fall in elevation (in Wh/m, i.e., Watt-hours per meter).

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util"><code>Map</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>, <wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-empiricalconsumptionmodel#freeFlowSpeedTable" class="member-name-link"><code>freeFlowSpeedTable</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Free flow speed table describes energy consumption when traveling at constant speed.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util"><code>Map</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>, <wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-empiricalconsumptionmodel#trafficSpeedTable" class="member-name-link"><code>trafficSpeedTable</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Traffic speed table describes energy consumption when traveling under heavy traffic conditions, i.e.

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

      EmpiricalConsumptionModel ()

  </div>

  <div class="col-last even-row-color">

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

  - <div id="sdk-for-android-navigate-ascentConsumptionInWattHoursPerMeter" class="section detail">

    ### ascentConsumptionInWattHoursPerMeter

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">ascentConsumptionInWattHoursPerMeter</span>

    </div>

    <div class="block">

    Rate of energy consumed per meter rise in elevation (in Wh/m, i.e., Watt-hours per meter).

    </div>

    </div>

  - <div id="sdk-for-android-navigate-descentRecoveryInWattHoursPerMeter" class="section detail">

    ### descentRecoveryInWattHoursPerMeter

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">descentRecoveryInWattHoursPerMeter</span>

    </div>

    <div class="block">

    Rate of energy recovered per meter fall in elevation (in Wh/m, i.e., Watt-hours per meter).

    </div>

    </div>

  - <div id="sdk-for-android-navigate-freeFlowSpeedTable" class="section detail">

    ### freeFlowSpeedTable

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util">Map</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a>,<wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a>\></span> <span class="element-name">freeFlowSpeedTable</span>

    </div>

    <div class="block">

    Free flow speed table describes energy consumption when traveling at constant speed. It defines a function curve specifying consumption rate at a given free flow speed on a flat stretch of road. Map keys represent speed values that are non-negative integers in units of (km/h). Map values represent consumption values that are non-negative floating point values in units of (Wh/m). The function is linearly interpolated between each successive pair of data points: For values below the first list value, the first value is used. For values after the last list value, the last list value is used. At minimum, one key/value pair must be set. In this case the consumption value is used for all possible speed keys.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-trafficSpeedTable" class="section detail">

    ### trafficSpeedTable

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util">Map</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a>,<wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a>\></span> <span class="element-name">trafficSpeedTable</span>

    </div>

    <div class="block">

    Traffic speed table describes energy consumption when traveling under heavy traffic conditions, i.e. when the vehicle is expected to often change the travel speed. It defines a function curve specifying consumption rate at a given speed under traffic conditions on a flat stretch of road. Map keys represent traffic speed values that are non-negative integers in units of (km/h). Map values represent consumption values that are non-negative floating point values in units of (Wh/m). The function is linearly interpolated between each successive pair of data points: For values below the first list value, the first value is used. For values after the last list value, the last list value is used. If only one key/value pair is set, the consumption value is used for all possible traffic speed keys. If trafficSpeedTable is empty then only freeFlowSpeedTable is used for calculating speed-related energy consumption.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-auxiliaryConsumptionInWattHoursPerSecond" class="section detail">

    ### auxiliaryConsumptionInWattHoursPerSecond

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">auxiliaryConsumptionInWattHoursPerSecond</span>

    </div>

    <div class="block">

    Rate of energy (in Wh/s) consumed by the vehicle's auxiliary systems (e.g., air conditioning, lights) per second of travel.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### EmpiricalConsumptionModel

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">EmpiricalConsumptionModel</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

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

