---
title: "TrafficOnSection (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-trafficonsection"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.TrafficOnSection

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">TrafficOnSection</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Traffic information on a section.

</div>

</div>

<div class="section summary">

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

  [`RoutePlace`](sdk-for-android-explore-com-here-sdk-routing-routeplace "class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-trafficonsection#arrivalPlace"
  class="member-name-link"><code>arrivalPlace</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Describes the arrival place.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`RoutePlace`](sdk-for-android-explore-com-here-sdk-routing-routeplace "class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-trafficonsection#departurePlace"
  class="member-name-link"><code>departurePlace</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Describes the departure place.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`GeoCoordinates`](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")`>`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-trafficonsection#geometry"
  class="member-name-link"><code>geometry</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  List of coordinates representing the polyline of this section.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`TrafficIncidentOnRoute`](sdk-for-android-explore-com-here-sdk-routing-trafficincidentonroute "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-trafficonsection#trafficIncidents"
  class="member-name-link"><code>trafficIncidents</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  List of traffic incidents.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`TrafficOnSpan`](sdk-for-android-explore-com-here-sdk-routing-trafficonspan "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-trafficonsection#trafficSpans"
  class="member-name-link"><code>trafficSpans</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  List of traffic spans.

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

      TrafficOnSection(RoutePlace departurePlace,
       RoutePlace arrivalPlace)

  </div>

  <div class="col-last even-row-color">

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals(Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode()

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
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
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

- <div id="sdk-for-android-explore-field-detail"
  class="section field-details">

  - <div id="sdk-for-android-explore-geometry" class="section detail">

    ### geometry

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")></span> <span class="element-name">geometry</span>

    </div>

    <div class="block">

    List of coordinates representing the polyline of this section.

    </div>

    </div>

  - <div id="sdk-for-android-explore-trafficSpans"
    class="section detail">

    ### trafficSpans

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[TrafficOnSpan](sdk-for-android-explore-com-here-sdk-routing-trafficonspan "class in com.here.sdk.routing")></span> <span class="element-name">trafficSpans</span>

    </div>

    <div class="block">

    List of traffic spans.

    </div>

    </div>

  - <div id="sdk-for-android-explore-trafficIncidents"
    class="section detail">

    ### trafficIncidents

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[TrafficIncidentOnRoute](sdk-for-android-explore-com-here-sdk-routing-trafficincidentonroute "class in com.here.sdk.routing")></span> <span class="element-name">trafficIncidents</span>

    </div>

    <div class="block">

    List of traffic incidents.

    </div>

    </div>

  - <div id="sdk-for-android-explore-departurePlace"
    class="section detail">

    ### departurePlace

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[RoutePlace](sdk-for-android-explore-com-here-sdk-routing-routeplace "class in com.here.sdk.routing")</span> <span class="element-name">departurePlace</span>

    </div>

    <div class="block">

    Describes the departure place.

    </div>

    </div>

  - <div id="sdk-for-android-explore-arrivalPlace"
    class="section detail">

    ### arrivalPlace

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[RoutePlace](sdk-for-android-explore-com-here-sdk-routing-routeplace "class in com.here.sdk.routing")</span> <span class="element-name">arrivalPlace</span>

    </div>

    <div class="block">

    Describes the arrival place.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.routing.RoutePlace,com.here.sdk.routing.RoutePlace)"
    class="section detail">

    ### TrafficOnSection

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TrafficOnSection</span><span class="parameters">(@NonNull
    [RoutePlace](sdk-for-android-explore-com-here-sdk-routing-routeplace "class in com.here.sdk.routing") departurePlace,
    @NonNull
    [RoutePlace](sdk-for-android-explore-com-here-sdk-routing-routeplace "class in com.here.sdk.routing") arrivalPlace)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `departurePlace` -

    Describes the departure place.

    `arrivalPlace` -

    Describes the arrival place.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-equals(java.lang.Object)"
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

  - <div id="sdk-for-android-explore-hashCode()" class="section detail">

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

</div>

