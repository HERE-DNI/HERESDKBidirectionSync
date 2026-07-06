---
title: "TransitRouteOptions (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-transitrouteoptions"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.TransitRouteOptions

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">TransitRouteOptions</span>
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

All the options to specify how a public transit route should be
calculated.

</div>

</div>

<div class="section summary">
<div id="sdk-for-android-explore-field-summary"
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

  `int`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-transitrouteoptions#alternatives" class="member-name-link"><code>alternatives</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Number of alternative routes to return aside from the optimal route.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-transitrouteoptions#arrivalTime" class="member-name-link"><code>arrivalTime</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional time when travel is expected to end.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-transitrouteoptions#changes" class="member-name-link"><code>changes</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Maximum number of changes or transfers allowed in a route.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-transitrouteoptions#departureTime" class="member-name-link"><code>departureTime</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional time when travel is expected to start.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`TransitModeFilter`](sdk-for-android-explore-com-here-sdk-routing-transitmodefilter "enum class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-transitrouteoptions#modeFilter" class="member-name-link"><code>modeFilter</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Defines inclusion or exclusion of transit modes for route calculation.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`TransitMode`](sdk-for-android-explore-com-here-sdk-routing-transitmode "enum class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-transitrouteoptions#modes" class="member-name-link"><code>modes</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  This list is used to determine which transit modes should be used for
  route calculation, modeFilter specifies whether this list is an
  inclusion or an exclusion.

  </div>

  </div>

  <div class="col-first even-row-color">

  `int`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-transitrouteoptions#pedestrianMaxDistanceInMeters" class="member-name-link"><code>pedestrianMaxDistanceInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Maximum allowed walking distance in meters (e.g.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-transitrouteoptions#pedestrianSpeedInMetersPerSecond" class="member-name-link"><code>pedestrianSpeedInMetersPerSecond</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Walking speed in meters per second.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`RouteTextOptions`](sdk-for-android-explore-com-here-sdk-routing-routetextoptions "class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-transitrouteoptions#textOptions" class="member-name-link"><code>textOptions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Customize textual content returned from the route calculation, such as
  localization, format, and unit system.

  </div>

  </div>

  </div>

  </div>
<div id="sdk-for-android-explore-constructor-summary"
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

      TransitRouteOptions()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>
<div id="sdk-for-android-explore-method-summary"
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

      equals(Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`TransitRouteOptions`](sdk-for-android-explore-com-here-sdk-routing-transitrouteoptions "class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      fromDefaultParameterConfiguration()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns TransitRouteOptions instance with default values used in SDK.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-field-detail"
  class="section field-details">
<div id="sdk-for-android-explore-departureTime"
    class="section detail">

    ### departureTime

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">departureTime</span>

    </div>

    <div class="block">

    Optional time when travel is expected to start. If it is not
    specified, it is set to the current time.

    </div>

    </div>
<div id="sdk-for-android-explore-arrivalTime"
    class="section detail">

    ### arrivalTime

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">arrivalTime</span>

    </div>

    <div class="block">

    Optional time when travel is expected to end.

    </div>

    </div>
<div id="sdk-for-android-explore-alternatives"
    class="section detail">

    ### alternatives

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">alternatives</span>

    </div>

    <div class="block">

    Number of alternative routes to return aside from the optimal route.
    The provided value must be in the range \[0, 6\]. By default, it is
    0 and only one route is calculated.

    </div>

    </div>
<div id="sdk-for-android-explore-changes" class="section detail">

    ### changes

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">changes</span>

    </div>

    <div class="block">

    Maximum number of changes or transfers allowed in a route. When it
    is not set, unlimited number of changes is permitted. The provided
    value must be in the range \[0, 6\].

    </div>

    </div>
<div id="sdk-for-android-explore-modeFilter" class="section detail">

    ### modeFilter

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TransitModeFilter](sdk-for-android-explore-com-here-sdk-routing-transitmodefilter "enum class in com.here.sdk.routing")</span> <span class="element-name">modeFilter</span>

    </div>

    <div class="block">

    Defines inclusion or exclusion of transit modes for route
    calculation. By default, the inclusion mode is used.

    </div>

    </div>
<div id="sdk-for-android-explore-modes" class="section detail">

    ### modes

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[TransitMode](sdk-for-android-explore-com-here-sdk-routing-transitmode "enum class in com.here.sdk.routing")\></span> <span class="element-name">modes</span>

    </div>

    <div class="block">

    This list is used to determine which transit modes should be used
    for route calculation, modeFilter specifies whether this list is an
    inclusion or an exclusion. For example, specifying subway and bus
    transit modes with the include filter, returns only subway and bus
    transit modes, and with the exclude filter, returns all the transit
    modes except subway and bus. When not set, all the supported transit
    modes are permitted. By default, this list is empty.

    </div>

    </div>
<div id="sdk-for-android-explore-pedestrianSpeedInMetersPerSecond"
    class="section detail">

    ### pedestrianSpeedInMetersPerSecond

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">pedestrianSpeedInMetersPerSecond</span>

    </div>

    <div class="block">

    Walking speed in meters per second. Influences the duration of
    walking segments from origin to a station, from a station to
    destination and in-between the stations (e.g. if transfer is
    needed). The provided value must be in the range \[0.5, 2.0\]. The
    default value is 1.0 mps.

    </div>

    </div>
<div id="sdk-for-android-explore-pedestrianMaxDistanceInMeters"
    class="section detail">

    ### pedestrianMaxDistanceInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">pedestrianMaxDistanceInMeters</span>

    </div>

    <div class="block">

    Maximum allowed walking distance in meters (e.g. when looking for
    nearest stations). The provided value must be in the range \[0,
    6000\]. The default value is 2000 meters.

    </div>

    </div>
<div id="sdk-for-android-explore-textOptions"
    class="section detail">

    ### textOptions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[RouteTextOptions](sdk-for-android-explore-com-here-sdk-routing-routetextoptions "class in com.here.sdk.routing")</span> <span class="element-name">textOptions</span>

    </div>

    <div class="block">

    Customize textual content returned from the route calculation, such
    as localization, format, and unit system.

    </div>

    </div>

  </div>
<div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">
<div id="sdk-for-android-explore-<init>()" class="section detail">

    ### TransitRouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TransitRouteOptions</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  </div>
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-equals(java.lang.Object)"
    class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in
    class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>
<div id="sdk-for-android-explore-hashCode()" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in
    class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>
<div id="sdk-for-android-explore-fromDefaultParameterConfiguration()"
    class="section detail">

    ### fromDefaultParameterConfiguration

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[TransitRouteOptions](sdk-for-android-explore-com-here-sdk-routing-transitrouteoptions "class in com.here.sdk.routing")</span> <span class="element-name">fromDefaultParameterConfiguration</span>()

    </div>

    <div class="block">

    Returns TransitRouteOptions instance with default values used in
    SDK.

    </div>

    Returns:  
    An
    [`TransitRouteOptions`](sdk-for-android-explore-com-here-sdk-routing-transitrouteoptions "class in com.here.sdk.routing")
    instance with default values used in SDK.

    </div>

  </div>

</div>

