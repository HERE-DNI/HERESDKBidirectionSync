---
title: "PolylineSimplifier.Options (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-core-package-summary">com.here.sdk.core</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.core.PolylineSimplifier.Options → com.here.sdk.core.PolylineSimplifier.Options

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

Enclosing class:  
<a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier" title="class in com.here.sdk.core">PolylineSimplifier</a>

<div class="type-signature">

<span class="modifiers">public static final class </span><span class="element-name type-name-label">PolylineSimplifier.Options</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Controls the strategy of PolylineSimplifier.simplify(java.util.List\<com.here.sdk.core.GeoCoordinates\>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback) when reducing a size of polyline.

</div>

</div>

- <div id="sdk-for-android-explore-field-summary" class="section field-summary">

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

  `long`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#maxPoints" class="member-name-link"><code>maxPoints</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Sets the upper limit on the resulting collection for the PolylineSimplifier.simplify(java.util.List\<com.here.sdk.core.GeoCoordinates\>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback) .

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final long`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL" class="member-name-link"><code>SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Value for simplification tolerance for 14 zoom level without significant artifacts.

  </div>

  </div>

  <div class="col-first even-row-color">

  `long`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters" class="member-name-link"><code>simplificationToleranceInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Sets the accuracy limit for the PolylineSimplifier.simplify(java.util.List\<com.here.sdk.core.GeoCoordinates\>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback) : higher tolerance results in more simplification (fewer points); lower tolerance keeps the line closer to its original shape.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary" class="section constructor-summary">

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

      Options ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates default options with maxPoints equal to 0 and simplificationToleranceInMeters equal to SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL .

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      Options (long maxPoints,
       long simplificationToleranceInMeters)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates options with explicitly specified maxPoints and simplificationToleranceInMeters .

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL" class="section detail">

    ### SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">long</span> <span class="element-name">SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL</span>

    </div>

    <div class="block">

    Value for simplification tolerance for 14 zoom level without significant artifacts.

    </div>

    See Also:  
    - <a href="sdk-for-android-explore-constant-values#com.here.sdk.core.PolylineSimplifier.Options.SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL">Constant Field Values</a>

    </div>

  - <div id="sdk-for-android-explore-maxPoints" class="section detail">

    ### maxPoints

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">maxPoints</span>

    </div>

    <div class="block">

    Sets the upper limit on the resulting collection for the PolylineSimplifier.simplify(java.util.List\<com.here.sdk.core.GeoCoordinates\>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback) . Lower value results in the lower accuracy of the resulting polyline. If maxPoints is less than 2 then resulting polyline will not have an upper limit on the size and only simplificationToleranceInMeters will be considered. When maxPoints is greater than size of the passed polyline then simplification algorithm will take into account only simplificationToleranceInMeters .

    </div>

    </div>

  - <div id="sdk-for-android-explore-simplificationToleranceInMeters" class="section detail">

    ### simplificationToleranceInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">simplificationToleranceInMeters</span>

    </div>

    <div class="block">

    Sets the accuracy limit for the PolylineSimplifier.simplify(java.util.List\<com.here.sdk.core.GeoCoordinates\>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback) : higher tolerance results in more simplification (fewer points); lower tolerance keeps the line closer to its original shape. If removing a point produces polyline, which deviates from the original one more than simplificationToleranceInMeters , then this point is left in the collection. If specified tolerance will not allow to create a polyline conforming to maxPoints , then simplificationToleranceInMeters is ignored. Default value is equal to SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL .

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init" class="section detail">

    ### Options

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Options</span>()

    </div>

    <div class="block">

    Creates default options with maxPoints equal to 0 and simplificationToleranceInMeters equal to SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-init-long-long" class="section detail">

    ### Options

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Options</span><wbr></wbr><span class="parameters">(long maxPoints, long simplificationToleranceInMeters)</span>

    </div>

    <div class="block">

    Creates options with explicitly specified maxPoints and simplificationToleranceInMeters .

    </div>

    Parameters:  
    `maxPoints` -

    Sets the upper limit on the resulting collection for the [](sdk-for-android-explore-com-here-sdk-core-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback))

        PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)

    </a>. Lower value results in the lower accuracy of the resulting polyline. If `maxPoints` is less than `2` then resulting polyline will not have an upper limit on the size and only <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters">`simplificationToleranceInMeters`</a> will be considered. When `maxPoints` is greater than size of the passed polyline then simplification algorithm will take into account only <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#simplificationToleranceInMeters">`simplificationToleranceInMeters`</a>.

    </p>

    `simplificationToleranceInMeters` -

    Sets the accuracy limit for the [](sdk-for-android-explore-com-here-sdk-core-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback))

        PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)

    </a>:

    - higher tolerance results in more simplification (fewer points);
    - lower tolerance keeps the line closer to its original shape.

    If removing a point produces polyline, which deviates from the original one more than `simplificationToleranceInMeters`, then this point is left in the collection. If specified tolerance will not allow to create a polyline conforming to <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#maxPoints">`maxPoints`</a>, then `simplificationToleranceInMeters` is ignored. Default value is equal to <a href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options#SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL">`SIMPLIFICATION_IN_METERS_14_ZOOM_LEVEL`</a>.

    </p>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

