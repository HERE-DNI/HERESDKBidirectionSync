---
title: "IndoorManeuver (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-indoormaneuver"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.routing.IndoorManeuver → com.here.NativeBase com.here.sdk.routing.IndoorManeuver → com.here.sdk.routing.IndoorManeuver

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">IndoorManeuver</span> <span class="extends-implements">extends [NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Represents a maneuver within an indoor section.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`IndoorManeuverActions`](sdk-for-android-explore-com-here-sdk-routing-indoormaneuveractions "enum class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getAction ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the action type of this maneuver.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`GeoCoordinates`](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCoordinate ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the geographic coordinates of this maneuver.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDuration ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the duration to complete this maneuver.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`IndoorLevelChangeData`](sdk-for-android-explore-com-here-sdk-routing-indoorlevelchangedata "class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getIndoorLevelChangeData ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the level change data for this maneuver.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`IndoorSpaceData`](sdk-for-android-explore-com-here-sdk-routing-indoorspacedata "class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getIndoorSpaceData ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the indoor space data for this maneuver.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `float`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLengthInMeters ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the length of this maneuver in meters.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLevelZIndex ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the vertical level index of this maneuver.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getOffset ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the offset of this maneuver from the start of the section.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSectionIndex ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the section index this maneuver belongs to.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-getAction" class="section detail">

    ### getAction

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[IndoorManeuverActions](sdk-for-android-explore-com-here-sdk-routing-indoormaneuveractions "enum class in com.here.sdk.routing")</span> <span class="element-name">getAction</span>()

    </div>

    <div class="block">

    Gets the action type of this maneuver.

    </div>

    Returns:  
    The action type of this maneuver.

    </div>

  - <div id="sdk-for-android-explore-getCoordinate" class="section detail">

    ### getCoordinate

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">getCoordinate</span>()

    </div>

    <div class="block">

    Gets the geographic coordinates of this maneuver.

    </div>

    Returns:  
    The geographic coordinates of this maneuver.

    </div>

  - <div id="sdk-for-android-explore-getOffset" class="section detail">

    ### getOffset

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getOffset</span>()

    </div>

    <div class="block">

    Gets the offset of this maneuver from the start of the section.

    </div>

    Returns:  
    The offset of this maneuver from the start of the section.

    </div>

  - <div id="sdk-for-android-explore-getSectionIndex" class="section detail">

    ### getSectionIndex

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getSectionIndex</span>()

    </div>

    <div class="block">

    Gets the section index this maneuver belongs to.

    </div>

    Returns:  
    The section index this maneuver belongs to.

    </div>

  - <div id="sdk-for-android-explore-getLengthInMeters" class="section detail">

    ### getLengthInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">float</span> <span class="element-name">getLengthInMeters</span>()

    </div>

    <div class="block">

    Gets the length of this maneuver in meters.

    </div>

    Returns:  
    The length of this maneuver in meters.

    </div>

  - <div id="sdk-for-android-explore-getDuration" class="section detail">

    ### getDuration

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">getDuration</span>()

    </div>

    <div class="block">

    Gets the duration to complete this maneuver.

    </div>

    Returns:  
    The duration to complete this maneuver.

    </div>

  - <div id="sdk-for-android-explore-getLevelZIndex" class="section detail">

    ### getLevelZIndex

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLevelZIndex</span>()

    </div>

    <div class="block">

    Gets the vertical level index of this maneuver.

    </div>

    Returns:  
    The vertical level index of this maneuver.

    </div>

  - <div id="sdk-for-android-explore-getIndoorSpaceData" class="section detail">

    ### getIndoorSpaceData

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[IndoorSpaceData](sdk-for-android-explore-com-here-sdk-routing-indoorspacedata "class in com.here.sdk.routing")</span> <span class="element-name">getIndoorSpaceData</span>()

    </div>

    <div class="block">

    Gets the indoor space data for this maneuver. This will be not null if the IndoorManeuverAction is ENTER_ACTION or LEAVE_ACTION.

    </div>

    Returns:  
    The indoor space data for this maneuver. This will be not null if the IndoorManeuverAction is ENTER_ACTION or LEAVE_ACTION.

    </div>

  - <div id="sdk-for-android-explore-getIndoorLevelChangeData" class="section detail">

    ### getIndoorLevelChangeData

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[IndoorLevelChangeData](sdk-for-android-explore-com-here-sdk-routing-indoorlevelchangedata "class in com.here.sdk.routing")</span> <span class="element-name">getIndoorLevelChangeData</span>()

    </div>

    <div class="block">

    Gets the level change data for this maneuver. This will be not null if the IndoorManeuverAction is LEVEL_CHANGE_ACTION.

    </div>

    Returns:  
    The level change data for this maneuver. This will be not null if the IndoorManeuverAction is LEVEL_CHANGE_ACTION.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

