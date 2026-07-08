---
title: "RefreshRouteParameters (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-refreshrouteparameters"
---

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.RefreshRouteParameters →
com.here.sdk.routing.RefreshRouteParameters

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">RefreshRouteParameters</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

This class provides the necessary information for refreshing a route
from a specific location on it.

</div>

</div>

- <div id="sdk-for-android-explore-field-summary"
  class="section field-summary">

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

  [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-refreshrouteparameters#routeHandle"
  class="member-name-link"><code>routeHandle</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The route handle holding the route to be refreshed.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`Waypoint`](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-refreshrouteparameters#startingPoint"
  class="member-name-link"><code>startingPoint</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Identify the new starting point of the route.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-refreshrouteparameters#startingSectionIndex"
  class="member-name-link"><code>startingSectionIndex</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates the index of the last traveled route section.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-refreshrouteparameters#traveledDistanceOnStartingSectionInMeters"
  class="member-name-link"><code>traveledDistanceOnStartingSectionInMeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Provides an indication on how much of the starting section is already
  traveled.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

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

      RefreshRouteParameters ( RouteHandle routeHandle,
       int startingSectionIndex,
       int traveledDistanceOnStartingSectionInMeters)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Create a new instance of RefreshRouteParameters with the point on the
  section of the route as a new starting point.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      RefreshRouteParameters ( RouteHandle routeHandle, Waypoint startingPoint)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Create a new instance of RefreshRouteParameters with the new starting
  point on the route.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      RefreshRouteParameters ( RouteHandle routeHandle, Waypoint startingPoint,
       int startingSectionIndex,
       int traveledDistanceOnStartingSectionInMeters)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Create a new instance of RefreshRouteParameters with the new starting
  point and the section position on the route.

  </div>

  </div>

  </div>

  </div>

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

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-field-detail"
  class="section field-details">

  - <div id="sdk-for-android-explore-routeHandle"
    class="section detail">

    ### routeHandle

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[RouteHandle](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing")</span> <span class="element-name">routeHandle</span>

    </div>

    <div class="block">

    The route handle holding the route to be refreshed.

    </div>

    </div>

  - <div id="sdk-for-android-explore-startingPoint"
    class="section detail">

    ### startingPoint

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")</span> <span class="element-name">startingPoint</span>

    </div>

    <div class="block">

    Identify the new starting point of the route. It should be of type
    WaypointType.STOPOVER . Otherwise, an RoutingError.INVALID_PARAMETER
    error is generated. Moreover, it should be very close to the
    original route specified with the RouteHandle . The location of this
    waypoint may by provided, for example, by a RouteProgress event.
    Since the new starting point is expected to be along the original
    route, the original route geometry is used to reach the remaining
    waypoints. The new route will not include the Waypoint items that
    lie behind the new starting point (i.e. the path that was already
    traveled). Plus, Route.getLengthInMeters() , Route.getDuration() ,
    and similar values are from the new starting point to the
    destination. If the new waypoint is too far off the original route,
    the route refresh may fail and an
    RoutingError.COULD_NOT_MATCH_ORIGIN error is triggered. In that
    case, an application may decide to calculate a new route from
    scratch.

    </div>

    </div>

  - <div id="sdk-for-android-explore-startingSectionIndex"
    class="section detail">

    ### startingSectionIndex

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">startingSectionIndex</span>

    </div>

    <div class="block">

    Indicates the index of the last traveled route section. When it is
    provided, the previous sections are discarded from the refreshed
    route and the starting point is searched in the provided section. If
    the starting point is not found in that section an
    RoutingError.COULD_NOT_MATCH_ORIGIN error is triggered.

    </div>

    </div>

  - <div id="sdk-for-android-explore-traveledDistanceOnStartingSectionInMeters"
    class="section detail">

    ### traveledDistanceOnStartingSectionInMeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">traveledDistanceOnStartingSectionInMeters</span>

    </div>

    <div class="block">

    Provides an indication on how much of the starting section is
    already traveled. The refresh route function would ignore the first
    part of the section. If it is provided with an invalid starting
    section index, an RoutingError.INVALID_PARAMETER error is generated.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-RouteHandle-com-here-sdk-routing-Waypoint"
    class="section detail">

    ### RefreshRouteParameters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RefreshRouteParameters</span><span class="parameters">(@NonNull
    [RouteHandle](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing") routeHandle,
    @NonNull
    [Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing") startingPoint)</span>

    </div>

    <div class="block">

    Create a new instance of RefreshRouteParameters with the new
    starting point on the route.

    </div>

    Parameters:  
    `routeHandle` -

    The route handle holding the route to be refreshed.

    `startingPoint` -

    Identify the new starting point of the route.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-RouteHandle-int-int"
    class="section detail">

    ### RefreshRouteParameters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RefreshRouteParameters</span><span class="parameters">(@NonNull
    [RouteHandle](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing") routeHandle,
    int startingSectionIndex,
    int traveledDistanceOnStartingSectionInMeters)</span>

    </div>

    <div class="block">

    Create a new instance of RefreshRouteParameters with the point on
    the section of the route as a new starting point.

    </div>

    Parameters:  
    `routeHandle` -

    The route handle holding the route to be refreshed.

    `startingSectionIndex` -

    Indicates the index of the last traveled route section.

    `traveledDistanceOnStartingSectionInMeters` -

    Provides an indication on how much of the starting section is
    already traveled.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-RouteHandle-com-here-sdk-routing-Waypoint-int-int"
    class="section detail">

    ### RefreshRouteParameters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RefreshRouteParameters</span><span class="parameters">(@NonNull
    [RouteHandle](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing") routeHandle,
    @NonNull
    [Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing") startingPoint,
    int startingSectionIndex,
    int traveledDistanceOnStartingSectionInMeters)</span>

    </div>

    <div class="block">

    Create a new instance of RefreshRouteParameters with the new
    starting point and the section position on the route.

    </div>

    Parameters:  
    `routeHandle` -

    The route handle holding the route to be refreshed.

    `startingPoint` -

    Identify the new starting point of the route.

    `startingSectionIndex` -

    Indicates the index of the last traveled route section.

    `traveledDistanceOnStartingSectionInMeters` -

    Provides an indication on how much of the starting section is
    already traveled.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-equals-java-lang-Object"
    class="section detail">

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

  - <div id="sdk-for-android-explore-hashCode" class="section detail">

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

