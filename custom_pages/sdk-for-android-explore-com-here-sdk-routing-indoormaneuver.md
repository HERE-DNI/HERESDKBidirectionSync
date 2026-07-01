---
title: "IndoorManeuver (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-indoormaneuver"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.routing.IndoorManeuver →
com.here.NativeBase → com.here.sdk.routing.IndoorManeuver

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">IndoorManeuver</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Represents a maneuver within an indoor section.

</div>

</div>

<div class="section summary">

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
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-indoormaneuveractions"
  title="enum class in com.here.sdk.routing"><code>IndoorManeuverActions</code></a></td>
  <td><pre><code>getAction()</code></pre></td>
  <td><div class="block">
  Gets the action type of this maneuver.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a></td>
  <td><pre><code>getCoordinate()</code></pre></td>
  <td><div class="block">
  Gets the geographic coordinates of this maneuver.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-time-duration"
  title="class in com.here.time"><code>Duration</code></a></td>
  <td><pre><code>getDuration()</code></pre></td>
  <td><div class="block">
  Gets the duration to complete this maneuver.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-indoorlevelchangedata"
  title="class in com.here.sdk.routing"><code>IndoorLevelChangeData</code></a></td>
  <td><pre><code>getIndoorLevelChangeData()</code></pre></td>
  <td><div class="block">
  Gets the level change data for this maneuver.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-indoorspacedata"
  title="class in com.here.sdk.routing"><code>IndoorSpaceData</code></a></td>
  <td><pre><code>getIndoorSpaceData()</code></pre></td>
  <td><div class="block">
  Gets the indoor space data for this maneuver.
  </div></td>
  </tr>
  <tr>
  <td><code>float</code></td>
  <td><pre><code>getLengthInMeters()</code></pre></td>
  <td><div class="block">
  Gets the length of this maneuver in meters.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>getLevelZIndex()</code></pre></td>
  <td><div class="block">
  Gets the vertical level index of this maneuver.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>getOffset()</code></pre></td>
  <td><div class="block">
  Gets the offset of this maneuver from the start of the section.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>getSectionIndex()</code></pre></td>
  <td><div class="block">
  Gets the section index this maneuver belongs to.
  </div></td>
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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
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

- <div id="method-detail" class="section method-details">

  - <div id="getAction()" class="section detail">

    ### getAction

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[IndoorManeuverActions](sdk-for-android-explore-com-here-sdk-routing-indoormaneuveractions "enum class in com.here.sdk.routing")</span> <span class="element-name">getAction</span>()

    </div>

    <div class="block">

    Gets the action type of this maneuver.

    </div>

    Returns:  
    The action type of this maneuver.

    </div>

  - <div id="getCoordinate()" class="section detail">

    ### getCoordinate

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">getCoordinate</span>()

    </div>

    <div class="block">

    Gets the geographic coordinates of this maneuver.

    </div>

    Returns:  
    The geographic coordinates of this maneuver.

    </div>

  - <div id="getOffset()" class="section detail">

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

  - <div id="getSectionIndex()" class="section detail">

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

  - <div id="getLengthInMeters()" class="section detail">

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

  - <div id="getDuration()" class="section detail">

    ### getDuration

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">getDuration</span>()

    </div>

    <div class="block">

    Gets the duration to complete this maneuver.

    </div>

    Returns:  
    The duration to complete this maneuver.

    </div>

  - <div id="getLevelZIndex()" class="section detail">

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

  - <div id="getIndoorSpaceData()" class="section detail">

    ### getIndoorSpaceData

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[IndoorSpaceData](sdk-for-android-explore-com-here-sdk-routing-indoorspacedata "class in com.here.sdk.routing")</span> <span class="element-name">getIndoorSpaceData</span>()

    </div>

    <div class="block">

    Gets the indoor space data for this maneuver. This will be not null
    if the IndoorManeuverAction is ENTER_ACTION or LEAVE_ACTION.

    </div>

    Returns:  
    The indoor space data for this maneuver. This will be not null if
    the IndoorManeuverAction is ENTER_ACTION or LEAVE_ACTION.

    </div>

  - <div id="getIndoorLevelChangeData()" class="section detail">

    ### getIndoorLevelChangeData

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[IndoorLevelChangeData](sdk-for-android-explore-com-here-sdk-routing-indoorlevelchangedata "class in com.here.sdk.routing")</span> <span class="element-name">getIndoorLevelChangeData</span>()

    </div>

    <div class="block">

    Gets the level change data for this maneuver. This will be not null
    if the IndoorManeuverAction is LEVEL_CHANGE_ACTION.

    </div>

    Returns:  
    The level change data for this maneuver. This will be not null if
    the IndoorManeuverAction is LEVEL_CHANGE_ACTION.

    </div>

  </div>

</div>

