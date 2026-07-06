---
title: "Maneuver (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-maneuver"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.routing.Maneuver →
com.here.NativeBase → com.here.sdk.routing.Maneuver

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">Maneuver</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

This class provides all the information for a maneuver. The directional
information (e.g. road names, road numbers and signpost direction) is
stored in getRoadTexts() and getNextRoadTexts() attributes. As for the
motorway exit information, it can be obtained from getExitSignTexts()
attribute.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

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

  [`ManeuverAction`](sdk-for-android-explore-com-here-sdk-routing-maneuveraction "enum class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getAction()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the maneuver action.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`GeoCoordinates`](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCoordinates()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the geographic coordinates where the maneuver is located.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCountryCode()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the country code of the maneuver position.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDuration()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the estimated time in seconds needed to perform the maneuver.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`LocalizedTexts`](sdk-for-android-explore-com-here-sdk-core-localizedtexts "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getExitSignTexts()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the textual attributes of the exit sign.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`LocalizedTexts`](sdk-for-android-explore-com-here-sdk-core-localizedtexts "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getIntersectionNames()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the textual attributes of the intersection.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLengthInMeters()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the length of the maneuver in meters.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`RoadTexts`](sdk-for-android-explore-com-here-sdk-routing-roadtexts "class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getNextRoadTexts()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the textual attributes of the next road containing the
  corresponding road name(s) and road number(s) after the maneuver
  point.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getOffset()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the index over Section.getGeometry() where the maneuver is
  located.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`RoadTexts`](sdk-for-android-explore-com-here-sdk-routing-roadtexts "class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRoadTexts()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the textual attributes of the current road containing road names,
  road numbers and signpost direction (towards) information.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRoundaboutAngleInDegrees()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The angle is estimated between the incoming and outgoing route parts
  before entering the actual roundabout.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSectionIndex()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the index over Route.getSections() indicating the section to
  which the maneuver belongs to.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Signpost`](sdk-for-android-explore-com-here-sdk-routing-signpost "class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSignpost()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets Signpost object.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSpanIndex()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the index over Section.getSpans() indicating the first span after
  the maneuver point.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getText()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the maneuver instruction.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTurnAngleInDegrees()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the angle of the turn component of the maneuver.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-getAction()"
    class="section detail">

    ### getAction

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[ManeuverAction](sdk-for-android-explore-com-here-sdk-routing-maneuveraction "enum class in com.here.sdk.routing")</span> <span class="element-name">getAction</span>()

    </div>

    <div class="block">

    Gets the maneuver action.

    </div>

    Returns:  
    Indicates the maneuver action.

    </div>

  - <div id="sdk-for-android-explore-getCoordinates()"
    class="section detail">

    ### getCoordinates

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">getCoordinates</span>()

    </div>

    <div class="block">

    Gets the geographic coordinates where the maneuver is located.

    </div>

    Returns:  
    Geographic coordinates where the maneuver is located.

    </div>

  - <div id="sdk-for-android-explore-getOffset()"
    class="section detail">

    ### getOffset

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getOffset</span>()

    </div>

    <div class="block">

    Gets the index over Section.getGeometry() where the maneuver is
    located.

    </div>

    Returns:  
    Index over
    [](sdk-for-android-explore-com-here-sdk-routing-section#getGeometry())

        Section.getGeometry()

    where the maneuver is located.

    </div>

  - <div id="sdk-for-android-explore-getCountryCode()"
    class="section detail">

    ### getCountryCode

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getCountryCode</span>()

    </div>

    <div class="block">

    Gets the country code of the maneuver position. The value is null
    when no data is available.

    </div>

    Returns:  
    The country code of the maneuver position. The value is `null` when
    no data is available.

    </div>

  - <div id="sdk-for-android-explore-getExitSignTexts()"
    class="section detail">

    ### getExitSignTexts

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[LocalizedTexts](sdk-for-android-explore-com-here-sdk-core-localizedtexts "class in com.here.sdk.core")</span> <span class="element-name">getExitSignTexts</span>()

    </div>

    <div class="block">

    Gets the textual attributes of the exit sign. These might contain
    exit number(s) and/or name(s). These attributes are only available
    for the Navigate license. Otherwise, the attributes are always
    empty.

    </div>

    Returns:  
    The textual attributes of the exit sign. These might contain exit
    number(s) and/or name(s).

    </div>

  - <div id="sdk-for-android-explore-getLengthInMeters()"
    class="section detail">

    ### getLengthInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLengthInMeters</span>()

    </div>

    <div class="block">

    Gets the length of the maneuver in meters.

    </div>

    Returns:  
    The length of the maneuver in meters.

    </div>

  - <div id="sdk-for-android-explore-getRoadTexts()"
    class="section detail">

    ### getRoadTexts

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[RoadTexts](sdk-for-android-explore-com-here-sdk-routing-roadtexts "class in com.here.sdk.routing")</span> <span class="element-name">getRoadTexts</span>()

    </div>

    <div class="block">

    Gets the textual attributes of the current road containing road
    names, road numbers and signpost direction (towards) information.
    Note: These attributes are only available for the Navigate license.
    Otherwise, the attributes are always empty.

    </div>

    Returns:  
    The textual attributes of the current road containing road names,
    road numbers and signpost direction (towards) information.

    </div>

  - <div id="sdk-for-android-explore-getNextRoadTexts()"
    class="section detail">

    ### getNextRoadTexts

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[RoadTexts](sdk-for-android-explore-com-here-sdk-routing-roadtexts "class in com.here.sdk.routing")</span> <span class="element-name">getNextRoadTexts</span>()

    </div>

    <div class="block">

    Gets the textual attributes of the next road containing the
    corresponding road name(s) and road number(s) after the maneuver
    point. These attributes are only available for the Navigate license.
    Otherwise, the attributes are always empty.

    </div>

    Returns:  
    The textual attributes of the next road containing the corresponding
    road name(s) and road number(s) after the maneuver point.

    </div>

  - <div id="sdk-for-android-explore-getSignpost()"
    class="section detail">

    ### getSignpost

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[Signpost](sdk-for-android-explore-com-here-sdk-routing-signpost "class in com.here.sdk.routing")</span> <span class="element-name">getSignpost</span>()

    </div>

    <div class="block">

    Gets Signpost object.

    </div>

    Returns:  
    Gets the
    [`Signpost`](sdk-for-android-explore-com-here-sdk-routing-signpost "class in com.here.sdk.routing")
    object.

    </div>

  - <div id="sdk-for-android-explore-getIntersectionNames()"
    class="section detail">

    ### getIntersectionNames

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[LocalizedTexts](sdk-for-android-explore-com-here-sdk-core-localizedtexts "class in com.here.sdk.core")</span> <span class="element-name">getIntersectionNames</span>()

    </div>

    <div class="block">

    Gets the textual attributes of the intersection. These attributes
    are only available for the Navigate license. Otherwise, the
    attributes are always empty. Note: Routes calculated with
    OfflineRoutingEngine are not supported.

    </div>

    Returns:  
    The textual attributes of the intersection.

    </div>

  - <div id="sdk-for-android-explore-getText()" class="section detail">

    ### getText

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getText</span>()

    </div>

    <div class="block">

    Gets the maneuver instruction. The text is formatted and localized
    as specified via RouteTextOptions . Note for users of the Navigate
    license: This text is meant to be displayed in a preview context,
    whereas real-time EventTextListener texts are meant to be used for
    spoken voice announcements during a trip.

    </div>

    Returns:  
    The maneuver instruction. The text is formatted and localized as
    specified via
    [`RouteTextOptions`](sdk-for-android-explore-com-here-sdk-routing-routetextoptions "class in com.here.sdk.routing").

    </div>

  - <div id="sdk-for-android-explore-getSectionIndex()"
    class="section detail">

    ### getSectionIndex

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getSectionIndex</span>()

    </div>

    <div class="block">

    Gets the index over Route.getSections() indicating the section to
    which the maneuver belongs to.

    </div>

    Returns:  
    Index over
    [](sdk-for-android-explore-com-here-sdk-routing-route#getSections())

        Route.getSections()

    indicating the section to which the maneuver belongs to.

    </div>

  - <div id="sdk-for-android-explore-getSpanIndex()"
    class="section detail">

    ### getSpanIndex

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getSpanIndex</span>()

    </div>

    <div class="block">

    Gets the index over Section.getSpans() indicating the first span
    after the maneuver point. Note: The span index for the last
    maneuvers (those maneuvers with maneuver action set to
    ManeuverAction.ARRIVE ) cannot be used, since these maneuvers are
    placed after the last span of the route and the span index for them
    would be greater than the span list size.

    </div>

    Returns:  
    Index over
    [](sdk-for-android-explore-com-here-sdk-routing-section#getSpans())

        Section.getSpans()

    indicating the first span after the maneuver point.

    </div>

  - <div id="sdk-for-android-explore-getDuration()"
    class="section detail">

    ### getDuration

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">getDuration</span>()

    </div>

    <div class="block">

    Gets the estimated time in seconds needed to perform the maneuver.

    </div>

    Returns:  
    The estimated time in seconds needed to perform the maneuver.

    </div>

  - <div id="sdk-for-android-explore-getTurnAngleInDegrees()"
    class="section detail">

    ### getTurnAngleInDegrees

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getTurnAngleInDegrees</span>()

    </div>

    <div class="block">

    Gets the angle of the turn component of the maneuver. The value is
    in degrees and from -180 to 180. The angle increases clockwise and
    small values are used for going straight, i.e. a positive number
    means there is a right turn and a negative number is a left turn.
    Some maneuvers like Depart, Arrive and Roundabout pass doesn't have
    a well defined angle, so the value is omitted. Note: These
    attributes are only available for the Navigate license.

    </div>

    Returns:  
    The angle of the turn component of the maneuver.

    </div>

  - <div id="sdk-for-android-explore-getRoundaboutAngleInDegrees()"
    class="section detail">

    ### getRoundaboutAngleInDegrees

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getRoundaboutAngleInDegrees</span>()

    </div>

    <div class="block">

    The angle is estimated between the incoming and outgoing route parts
    before entering the actual roundabout. This is done to provide a
    better orientation for drivers. For better results, the incoming and
    outcoming route parts can be around 50 meters in length. In
    addition, these parts lie usually around 30 meters away from the
    actual roundabout. Therefore, the resulting arc does not necessarily
    represent the exact curved path a vehicle has to follow within a
    roundabout from the point of entry to the point of exit. Instead, it
    reflects the route path before and after the roundabout to highlight
    the directional change along the route. The angle can have a value
    from -360.0 to 360.0, and it is positive in right-hand side driving
    country, and negative in left-hand side countries. Note that the
    value is available for both the enter roundabout actions and the
    exit roundabout actions. Both maneuvers have the same value. When
    the incoming or outgoing route parts are curvy or when the
    roundabout itself is not representing a perfect circle, then the
    accuracy of the angle may be compromised. Note: These attributes are
    only available for the Navigate license.

    </div>

    Returns:  
    The angle is estimated between the incoming and outgoing route parts
    before entering the actual roundabout.

    </div>

  </div>

</div>

