---
title: "TrafficOptimizationMode (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-routing-package-summary">com.here.sdk.routing</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object java.lang.Enum \< TrafficOptimizationMode \> com.here.sdk.routing.TrafficOptimizationMode → java.lang.Enum \< TrafficOptimizationMode \> com.here.sdk.routing.TrafficOptimizationMode → com.here.sdk.routing.TrafficOptimizationMode

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" class="external-link" title="class or interface in java.io"><code>Serializable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" class="external-link" title="class or interface in java.lang"><code>Comparable</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">`TrafficOptimizationMode`</a>`>`, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" class="external-link" title="class or interface in java.lang.constant"><code>Constable</code></a>

<div class="type-signature">

<span class="modifiers">public enum </span><span class="element-name type-name-label">TrafficOptimizationMode</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>\<<a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a>\></span>

</div>

<div class="block">

Traffic optimization mode that defines whether and what kind of traffic information should be considered during route calculation.

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary" class="section nested-class-summary">

  <div class="inherited-list">

  ## Nested classes/interfaces inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>Enum.EnumDesc</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>E</code></a>` extends `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang"><code>Enum</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>E</code></a>`>>`

  </div>

  </div>

- <div id="sdk-for-android-explore-enum-constant-summary" class="section constants-summary">

  ## Enum Constant Summary

  <div class="caption">

  Enum Constants

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Enum Constant

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode#DISABLED" class="member-name-link"><code>DISABLED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Traffic optimization is completely disabled, including long-term road closures.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode#LONG_TERM_CLOSURES_ONLY" class="member-name-link"><code>LONG_TERM_CLOSURES_ONLY</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Only long-term road closures are taken into account.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode#TIME_DEPENDENT" class="member-name-link"><code>TIME_DEPENDENT</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Traffic optimization is enabled, the shape of the route will be adjusted according to the traffic situation that depends on the RouteOptions.departureTime or RouteOptions.arrivalTime .

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">`TrafficOptimizationMode`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      valueOf ( String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns the enum constant of this class with the specified name.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">`TrafficOptimizationMode`</a>`[]`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      values ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns an array containing the constants of this enum class, in the order they are declared.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" class="external-link" title="class or interface in java.lang"><code>compareTo</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" class="external-link" title="class or interface in java.lang"><code>describeConstable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" class="external-link" title="class or interface in java.lang"><code>getDeclaringClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" class="external-link" title="class or interface in java.lang"><code>name</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" class="external-link" title="class or interface in java.lang"><code>ordinal</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" class="external-link" title="class or interface in java.lang"><code>valueOf</code></a>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-enum-constant-detail" class="section constant-details">

  ## Enum Constant Details

  - <div id="sdk-for-android-explore-TIME_DEPENDENT" class="section detail">

    ### TIME_DEPENDENT

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a></span> <span class="element-name">TIME_DEPENDENT</span>

    </div>

    <div class="block">

    Traffic optimization is enabled, the shape of the route will be adjusted according to the traffic situation that depends on the RouteOptions.departureTime or RouteOptions.arrivalTime . As a result, streets with heavy traffic will be avoided whenever possible. Note that this mode enables traffic-aware routing.

    </div>

    </div>

  - <div id="sdk-for-android-explore-LONG_TERM_CLOSURES_ONLY" class="section detail">

    ### LONG_TERM_CLOSURES_ONLY

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a></span> <span class="element-name">LONG_TERM_CLOSURES_ONLY</span>

    </div>

    <div class="block">

    Only long-term road closures are taken into account. Both RouteOptions.departureTime and RouteOptions.arrivalTime are ignored, and the route will be shaped disregarding all the available current and historical traffic information, except long-term road closures. Note that this mode disables traffic-aware routing regardless of other settings.

    </div>

    </div>

  - <div id="sdk-for-android-explore-DISABLED" class="section detail">

    ### DISABLED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a></span> <span class="element-name">DISABLED</span>

    </div>

    <div class="block">

    Traffic optimization is completely disabled, including long-term road closures. Both RouteOptions.departureTime and RouteOptions.arrivalTime are ignored, and the route will be shaped disregarding all the available current and historical traffic information. Note that seasonal closures are not excluded. To exclude seasonal closures, use RoadFeatures.SEASONAL_CLOSURE . Note that this mode disables traffic-aware routing regardless of other settings.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-values" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a>\[\]</span> <span class="element-name">values</span>()

    </div>

    <div class="block">

    Returns an array containing the constants of this enum class, in the order they are declared.

    </div>

    Returns:  
    an array containing the constants of this enum class, in the order they are declared

    </div>

  - <div id="sdk-for-android-explore-valueOf-java-lang-String" class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a></span> <span class="element-name">valueOf</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Returns the enum constant of this class with the specified name. The string must match exactly an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)

    </div>

    Parameters:  
    `name` - the name of the enum constant to be returned.

    Returns:  
    the enum constant with the specified name

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> - if this enum class has no constant with the specified name

    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" class="external-link" title="class or interface in java.lang"><code>NullPointerException</code></a> - if the argument is null

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

