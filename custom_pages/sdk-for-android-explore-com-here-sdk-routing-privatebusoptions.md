---
title: "PrivateBusOptions (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-privatebusoptions"
---

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.PrivateBusOptions →
com.here.sdk.routing.PrivateBusOptions

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html"
class="external-link"
title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public final class
</span><span class="element-name type-name-label">PrivateBusOptions</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="deprecation-block">

<span class="deprecated-label">Deprecated.</span>

<div class="deprecation-comment">

Will be removed in v4.28.0. Use `RoutingOptions` class instead.

</div>

</div>

<div class="block">

All the options to specify how a private bus route should be calculated.

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

  [`AllowOptions`](sdk-for-android-explore-com-here-sdk-routing-allowoptions "class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-privatebusoptions#allowOptions"
  class="member-name-link"><code>allowOptions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  The options explicitly allowed by user for route calculations.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`AvoidanceOptions`](sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions "class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-privatebusoptions#avoidanceOptions"
  class="member-name-link"><code>avoidanceOptions</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Options to specify restrictions for route calculations.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`BusSpecifications`](sdk-for-android-explore-com-here-sdk-transport-busspecifications "class in com.here.sdk.transport")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-privatebusoptions#busSpecifications"
  class="member-name-link"><code>busSpecifications</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Detailed bus specifications such as dimensions and weight.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-privatebusoptions#lastCharacterOfLicensePlate"
  class="member-name-link"><code>lastCharacterOfLicensePlate</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Specifies the last character of a vehicle's license plate, typically
  used to evaluate traffic restrictions in certain environmental or
  low-emission zones.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`MaxSpeedOnSegment`](sdk-for-android-explore-com-here-sdk-routing-maxspeedonsegment "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-privatebusoptions#maxSpeedOnSegments"
  class="member-name-link"><code>maxSpeedOnSegments</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Segments with restriction on maximum baseSpeed.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `int`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-privatebusoptions#occupantsNumber"
  class="member-name-link"><code>occupantsNumber</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Specifies the number of occupants in the vehicle, including driver,
  can affect the vehicle's ability to use HOV/carpool restricted lanes.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`RouteOptions`](sdk-for-android-explore-com-here-sdk-routing-routeoptions "class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-privatebusoptions#routeOptions"
  class="member-name-link"><code>routeOptions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Specifies the common route calculation options.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`RouteTextOptions`](sdk-for-android-explore-com-here-sdk-routing-routetextoptions "class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-privatebusoptions#textOptions"
  class="member-name-link"><code>textOptions</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Customize textual content returned from the route calculation, such as
  localization, format, and unit system.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`TollOptions`](sdk-for-android-explore-com-here-sdk-routing-tolloptions "class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-privatebusoptions#tollOptions"
  class="member-name-link"><code>tollOptions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Options to specify how the tolls should be calculated, such as
  transponders, vehicle category, and emission type.

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

      PrivateBusOptions ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Creates a new instance.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated.

  </div>

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated.

  </div>

   

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

  - <div id="sdk-for-android-explore-routeOptions"
    class="section detail">

    ### routeOptions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[RouteOptions](sdk-for-android-explore-com-here-sdk-routing-routeoptions "class in com.here.sdk.routing")</span> <span class="element-name">routeOptions</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Specifies the common route calculation options.

    </div>

    </div>

  - <div id="sdk-for-android-explore-textOptions"
    class="section detail">

    ### textOptions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[RouteTextOptions](sdk-for-android-explore-com-here-sdk-routing-routetextoptions "class in com.here.sdk.routing")</span> <span class="element-name">textOptions</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Customize textual content returned from the route calculation, such
    as localization, format, and unit system.

    </div>

    </div>

  - <div id="sdk-for-android-explore-avoidanceOptions"
    class="section detail">

    ### avoidanceOptions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[AvoidanceOptions](sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions "class in com.here.sdk.routing")</span> <span class="element-name">avoidanceOptions</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Options to specify restrictions for route calculations. By default
    no restrictions are applied.

    </div>

    </div>

  - <div id="sdk-for-android-explore-tollOptions"
    class="section detail">

    ### tollOptions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TollOptions](sdk-for-android-explore-com-here-sdk-routing-tolloptions "class in com.here.sdk.routing")</span> <span class="element-name">tollOptions</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Options to specify how the tolls should be calculated, such as
    transponders, vehicle category, and emission type.

    </div>

    </div>

  - <div id="sdk-for-android-explore-allowOptions"
    class="section detail">

    ### allowOptions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[AllowOptions](sdk-for-android-explore-com-here-sdk-routing-allowoptions "class in com.here.sdk.routing")</span> <span class="element-name">allowOptions</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    The options explicitly allowed by user for route calculations. By
    default no options are opt in.

    </div>

    </div>

  - <div id="sdk-for-android-explore-occupantsNumber"
    class="section detail">

    ### occupantsNumber

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">occupantsNumber</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Specifies the number of occupants in the vehicle, including driver,
    can affect the vehicle's ability to use HOV/carpool restricted
    lanes. Shouldn't be less than 1 or greater than 255. Defaults to 1.
    Note: This parameter has no effect unless HOV and/or HOT lane usage
    is enabled via allowOptions and such lanes are available in the
    selected country.

    </div>

    </div>

  - <div id="sdk-for-android-explore-lastCharacterOfLicensePlate"
    class="section detail">

    ### lastCharacterOfLicensePlate

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">lastCharacterOfLicensePlate</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Specifies the last character of a vehicle's license plate, typically
    used to evaluate traffic restrictions in certain environmental or
    low-emission zones. In cities like Bogotá, Mexico City, or Jakarta,
    specific license plate digits may be restricted on certain days or
    in certain areas to reduce congestion and emissions. When this value
    is provided, the HERE SDK considers it during route calculation to
    avoid roads or areas where your vehicle may be restricted based on
    local regulations. Example usage: "7", when the license plate of a
    vehicle looks like "B-ET-182487". If this value is not set, such
    license plate-based restrictions are ignored, and routing is
    performed without considering them.

    </div>

    </div>

  - <div id="sdk-for-android-explore-maxSpeedOnSegments"
    class="section detail">

    ### maxSpeedOnSegments

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[MaxSpeedOnSegment](sdk-for-android-explore-com-here-sdk-routing-maxspeedonsegment "class in com.here.sdk.routing")\></span> <span class="element-name">maxSpeedOnSegments</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Segments with restriction on maximum baseSpeed.

    </div>

    </div>

  - <div id="sdk-for-android-explore-busSpecifications"
    class="section detail">

    ### busSpecifications

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[BusSpecifications](sdk-for-android-explore-com-here-sdk-transport-busspecifications "class in com.here.sdk.transport")</span> <span class="element-name">busSpecifications</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Detailed bus specifications such as dimensions and weight. Note:
    Some members of bus_specifications have limited value range.
    BusSpecifications.grossWeightInKilograms must not be negative.
    BusSpecifications.heightInCentimeters must be in the range \[0,
    5000\]. BusSpecifications.widthInCentimeters must be in the range
    \[0, 5000\]. BusSpecifications.lengthInCentimeters must be in the
    range \[0, 30000\]. The validation of the range is done in the
    method that takes PrivateBusOptions as parameter.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-init" class="section detail">

    ### PrivateBusOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">PrivateBusOptions</span>()

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

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

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

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

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

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

