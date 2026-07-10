---
title: "RouteDeviation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-routedeviation"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.RouteDeviation → com.here.sdk.navigation.RouteDeviation

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">RouteDeviation</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Contains all the relevant information on a deviation from the route.

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

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation" title="class in com.here.sdk.navigation">`NavigableLocation`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviation#currentLocation" class="member-name-link"><code>currentLocation</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The current location.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation" title="class in com.here.sdk.navigation">`NavigableLocation`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviation#lastLocationOnRoute" class="member-name-link"><code>lastLocationOnRoute</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The last known location on the route.

  </div>

  </div>

  <div class="col-first even-row-color">

  `int`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviation#lastTraveledSectionIndex" class="member-name-link"><code>lastTraveledSectionIndex</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates the index of the last traveled route section.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `int`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviation#traveledDistanceOnLastSectionInMeters" class="member-name-link"><code>traveledDistanceOnLastSectionInMeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Offset in meter to the last visited position on the route section defined by the last traveled section index.

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

      RouteDeviation ( NavigableLocation lastLocationOnRoute,
       int lastTraveledSectionIndex,
       int traveledDistanceOnLastSectionInMeters, NavigableLocation currentLocation)

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

  - <div id="sdk-for-android-navigate-lastLocationOnRoute" class="section detail">

    ### lastLocationOnRoute

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a></span> <span class="element-name">lastLocationOnRoute</span>

    </div>

    <div class="block">

    The last known location on the route.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-lastTraveledSectionIndex" class="section detail">

    ### lastTraveledSectionIndex

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">lastTraveledSectionIndex</span>

    </div>

    <div class="block">

    Indicates the index of the last traveled route section.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-traveledDistanceOnLastSectionInMeters" class="section detail">

    ### traveledDistanceOnLastSectionInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">traveledDistanceOnLastSectionInMeters</span>

    </div>

    <div class="block">

    Offset in meter to the last visited position on the route section defined by the last traveled section index.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-currentLocation" class="section detail">

    ### currentLocation

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a></span> <span class="element-name">currentLocation</span>

    </div>

    <div class="block">

    The current location.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-com-here-sdk-navigation-NavigableLocation-int-int-com-here-sdk-navigation-NavigableLocation" class="section detail">

    ### RouteDeviation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RouteDeviation</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a> lastLocationOnRoute, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a> currentLocation)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `lastLocationOnRoute` -

    The last known location on the route.

    `lastTraveledSectionIndex` -

    Indicates the index of the last traveled route section.

    `traveledDistanceOnLastSectionInMeters` -

    Offset in meter to the last visited position on the route section defined by the last traveled section index.

    `currentLocation` -

    The current location.

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

