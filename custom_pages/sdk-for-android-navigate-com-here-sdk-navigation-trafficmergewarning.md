---
title: "TrafficMergeWarning (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarning"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.TrafficMergeWarning → com.here.sdk.navigation.TrafficMergeWarning

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">TrafficMergeWarning</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

A class that provides warning for merging traffic. The main field describing the merging traffic is TrafficMergeWarning.road_type specifying the type of road containing traffic which is merging with the current road. Use TrafficMergeWarningListener to get notifications about upcoming merging traffic.

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

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarning#distanceToTrafficMergeInMeters" class="member-name-link"><code>distanceToTrafficMergeInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Distance to merging traffic in meters.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">`DistanceType`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarning#distanceType" class="member-name-link"><code>distanceType</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The distance type for the warning, e.g.

  </div>

  </div>

  <div class="col-first even-row-color">

  `int`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarning#id" class="member-name-link"><code>id</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Unique identifier for this specific traffic merge warning instance.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `int`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarning#laneCount" class="member-name-link"><code>laneCount</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Number of lanes of the merging road containing the traffic.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergeroadtype" title="enum class in com.here.sdk.navigation">`TrafficMergeRoadType`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarning#roadType" class="member-name-link"><code>roadType</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Type of road which contains the merging traffic.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergeside" title="enum class in com.here.sdk.navigation">`TrafficMergeSide`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarning#side" class="member-name-link"><code>side</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The side from which the traffic is merging.

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

      TrafficMergeWarning (double distanceToTrafficMergeInMeters, DistanceType distanceType)

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

  - <div id="sdk-for-android-navigate-id" class="section detail">

    ### id

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">id</span>

    </div>

    <div class="block">

    Unique identifier for this specific traffic merge warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-distanceToTrafficMergeInMeters" class="section detail">

    ### distanceToTrafficMergeInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceToTrafficMergeInMeters</span>

    </div>

    <div class="block">

    Distance to merging traffic in meters.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-roadType" class="section detail">

    ### roadType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergeroadtype" title="enum class in com.here.sdk.navigation">TrafficMergeRoadType</a></span> <span class="element-name">roadType</span>

    </div>

    <div class="block">

    Type of road which contains the merging traffic.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-side" class="section detail">

    ### side

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergeside" title="enum class in com.here.sdk.navigation">TrafficMergeSide</a></span> <span class="element-name">side</span>

    </div>

    <div class="block">

    The side from which the traffic is merging.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-laneCount" class="section detail">

    ### laneCount

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">laneCount</span>

    </div>

    <div class="block">

    Number of lanes of the merging road containing the traffic. If the road has no lanes defined, than the number of lanes returned will be 1.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-distanceType" class="section detail">

    ### distanceType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></span> <span class="element-name">distanceType</span>

    </div>

    <div class="block">

    The distance type for the warning, e.g. a warning for a new traffic merge location ahead or a warning for passing a traffic merge location. Since the traffic merge warning is given relative to a single position on the route, DistanceType.REACHED will never be given for this warning.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-double-com-here-sdk-navigation-DistanceType" class="section detail">

    ### TrafficMergeWarning

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TrafficMergeWarning</span><wbr></wbr><span class="parameters">(double distanceToTrafficMergeInMeters, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `distanceToTrafficMergeInMeters` -

    Distance to merging traffic in meters.

    `distanceType` -

    The distance type for the warning, e.g. a warning for a new traffic merge location ahead or a warning for passing a traffic merge location. Since the traffic merge warning is given relative to a single position on the route, `DistanceType.REACHED` will never be given for this warning.

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

