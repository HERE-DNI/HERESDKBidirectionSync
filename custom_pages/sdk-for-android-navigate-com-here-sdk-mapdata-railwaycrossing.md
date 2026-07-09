---
title: "RailwayCrossing (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapdata-package-summary">com.here.sdk.mapdata</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.mapdata.RailwayCrossing → com.here.sdk.mapdata.RailwayCrossing

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">RailwayCrossing</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Identifies the presence and the location of railway corssings. Included in SegmentData only if SegmentDataLoaderOptions.loadRailwayCrossings is set to true .

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

  `int`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing#endOffsetInMeters" class="member-name-link"><code>endOffsetInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The end offset, in meters, from the beginning of the segment.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossingtype" title="enum class in com.here.sdk.mapdata">`RailwayCrossingType`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing#railwayCrossingType" class="member-name-link"><code>railwayCrossingType</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The type of barrier presented by the railway crossing.

  </div>

  </div>

  <div class="col-first even-row-color">

  `int`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing#startOffsetInMeters" class="member-name-link"><code>startOffsetInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The start offset, in meters, from the beginning of the segment.

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

      RailwayCrossing ( RailwayCrossingType railwayCrossingType)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-startOffsetInMeters" class="section detail">

    ### startOffsetInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">startOffsetInMeters</span>

    </div>

    <div class="block">

    The start offset, in meters, from the beginning of the segment. If endOffsetInMeters = 0, then startOffsetInMeters approximately indicates a middle of a railway crossing. If endOffsetInMeters \> 0, it means crossing consists of several rails, and startOffsetInMeters and endOffsetInMeters indicates starting and ending points of the crossing respectively. Default value is 0.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-endOffsetInMeters" class="section detail">

    ### endOffsetInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">endOffsetInMeters</span>

    </div>

    <div class="block">

    The end offset, in meters, from the beginning of the segment. Could be 0. See startOffsetInMeters description. Default value is 0.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-railwayCrossingType" class="section detail">

    ### railwayCrossingType

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossingtype" title="enum class in com.here.sdk.mapdata">RailwayCrossingType</a></span> <span class="element-name">railwayCrossingType</span>

    </div>

    <div class="block">

    The type of barrier presented by the railway crossing.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-com-here-sdk-mapdata-RailwayCrossingType" class="section detail">

    ### RailwayCrossing

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RailwayCrossing</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossingtype" title="enum class in com.here.sdk.mapdata">RailwayCrossingType</a> railwayCrossingType)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `railwayCrossingType` -

    The type of barrier presented by the railway crossing.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

