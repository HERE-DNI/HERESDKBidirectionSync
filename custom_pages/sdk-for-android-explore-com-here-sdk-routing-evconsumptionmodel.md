---
title: "EVConsumptionModel (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-evconsumptionmodel"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.EVConsumptionModel

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">EVConsumptionModel</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Parameters specific for the electric vehicle, which are then used to
calculate energy consumption on a given route. At minimum, you must
provide ascentConsumptionInWattHoursPerMeter ,
descentRecoveryInWattHoursPerMeter and a freeFlowSpeedTable .

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
  <td><code>double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evconsumptionmodel#ascentConsumptionInWattHoursPerMeter"
  class="member-name-link"><code>ascentConsumptionInWattHoursPerMeter</code></a></td>
  <td><div class="block">
  Rate of energy consumed per meter rise in elevation (in Wh/m, i.e.,
  Watt-hours per meter).
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evconsumptionmodel#auxiliaryConsumptionInWattHoursPerSecond"
  class="member-name-link"><code>auxiliaryConsumptionInWattHoursPerSecond</code></a></td>
  <td><div class="block">
  Rate of energy (in Wh/s) consumed by the vehicle's auxiliary systems
  (e.g., air conditioning, lights) per second of travel.
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evconsumptionmodel#descentRecoveryInWattHoursPerMeter"
  class="member-name-link"><code>descentRecoveryInWattHoursPerMeter</code></a></td>
  <td><div class="block">
  Rate of energy recovered per meter fall in elevation (in Wh/m, i.e.,
  Watt-hours per meter).
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
  class="external-link"
  title="class or interface in java.util"><code>Map</code></a><code>&lt;</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a><code>,</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evconsumptionmodel#freeFlowSpeedTable"
  class="member-name-link"><code>freeFlowSpeedTable</code></a></td>
  <td><div class="block">
  Free flow speed table describes energy consumption when traveling at
  constant speed.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
  class="external-link"
  title="class or interface in java.util"><code>Map</code></a><code>&lt;</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a><code>,</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evconsumptionmodel#trafficSpeedTable"
  class="member-name-link"><code>trafficSpeedTable</code></a></td>
  <td><div class="block">
  Traffic speed table describes energy consumption when traveling under
  heavy traffic conditions, i.e.
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
  <td><pre><code>EVConsumptionModel()</code></pre></td>
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

  - <div id="ascentConsumptionInWattHoursPerMeter"
    class="section detail">

    ### ascentConsumptionInWattHoursPerMeter

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">ascentConsumptionInWattHoursPerMeter</span>

    </div>

    <div class="block">

    Rate of energy consumed per meter rise in elevation (in Wh/m, i.e.,
    Watt-hours per meter).

    </div>

    </div>

  - <div id="descentRecoveryInWattHoursPerMeter" class="section detail">

    ### descentRecoveryInWattHoursPerMeter

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">descentRecoveryInWattHoursPerMeter</span>

    </div>

    <div class="block">

    Rate of energy recovered per meter fall in elevation (in Wh/m, i.e.,
    Watt-hours per meter).

    </div>

    </div>

  - <div id="freeFlowSpeedTable" class="section detail">

    ### freeFlowSpeedTable

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>></span> <span class="element-name">freeFlowSpeedTable</span>

    </div>

    <div class="block">

    Free flow speed table describes energy consumption when traveling at
    constant speed. It defines a function curve specifying consumption
    rate at a given free flow speed on a flat stretch of road. Map keys
    represent speed values that are non-negative integers in units of
    (km/h). Map values represent consumption values that are
    non-negative floating point values in units of (Wh/m). The function
    is linearly interpolated between each successive pair of data
    points: For values below the first list value, the first value is
    used. For values after the last list value, the last list value is
    used. At minimum, one key/value pair must be set. In this case the
    consumption value is used for all possible speed keys.

    </div>

    </div>

  - <div id="trafficSpeedTable" class="section detail">

    ### trafficSpeedTable

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>></span> <span class="element-name">trafficSpeedTable</span>

    </div>

    <div class="block">

    Traffic speed table describes energy consumption when traveling
    under heavy traffic conditions, i.e. when the vehicle is expected to
    often change the travel speed. It defines a function curve
    specifying consumption rate at a given speed under traffic
    conditions on a flat stretch of road. Map keys represent traffic
    speed values that are non-negative integers in units of (km/h). Map
    values represent consumption values that are non-negative floating
    point values in units of (Wh/m). The function is linearly
    interpolated between each successive pair of data points: For values
    below the first list value, the first value is used. For values
    after the last list value, the last list value is used. If only one
    key/value pair is set, the consumption value is used for all
    possible traffic speed keys. If trafficSpeedTable is empty then only
    freeFlowSpeedTable is used for calculating speed-related energy
    consumption.

    </div>

    </div>

  - <div id="auxiliaryConsumptionInWattHoursPerSecond"
    class="section detail">

    ### auxiliaryConsumptionInWattHoursPerSecond

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">auxiliaryConsumptionInWattHoursPerSecond</span>

    </div>

    <div class="block">

    Rate of energy (in Wh/s) consumed by the vehicle's auxiliary systems
    (e.g., air conditioning, lights) per second of travel.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### EVConsumptionModel

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">EVConsumptionModel</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

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

