---
title: "RouteOffset (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-routeoffset"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-routing-package-summary">com.here.sdk.routing</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.RouteOffset → com.here.sdk.routing.RouteOffset

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">RouteOffset</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents a specific location along the route. A RouteOffset is a location on the route defined by the section index and the distance in meters from the start of that section to the specified location on the route. An offset in meters indicates the distance that needs to be traveled to reach a specific location along the route, such as a railway crossing. For the latter case, the location of a railway crossing can be retrieved from RouteRailwayCrossing.coordinates .

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

  <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoffset#offsetInMeters" class="member-name-link"><code>offsetInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Offset from the start of the indexed Section to the specified location along the route.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `int`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoffset#sectionIndex" class="member-name-link"><code>sectionIndex</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Index of the corresponding route Section .

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

      RouteOffset (int sectionIndex,
       double offsetInMeters)

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

  - <div id="sdk-for-android-navigate-sectionIndex" class="section detail">

    ### sectionIndex

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">sectionIndex</span>

    </div>

    <div class="block">

    Index of the corresponding route Section . The start of the section indicates the start of the offset.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-offsetInMeters" class="section detail">

    ### offsetInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">offsetInMeters</span>

    </div>

    <div class="block">

    Offset from the start of the indexed Section to the specified location along the route. The maximum possible offset is limited by the length of the section and cannot exceed it.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-int-double" class="section detail">

    ### RouteOffset

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RouteOffset</span><wbr></wbr><span class="parameters">(int sectionIndex, double offsetInMeters)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `sectionIndex` -

    Index of the corresponding route <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing">`Section`</a>. The start of the section indicates the start of the offset.

    `offsetInMeters` -

    Offset from the start of the indexed <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing">`Section`</a> to the specified location along the route. The maximum possible offset is limited by the length of the section and cannot exceed it.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

