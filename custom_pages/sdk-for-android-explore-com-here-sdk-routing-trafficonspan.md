---
title: "TrafficOnSpan (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-trafficonspan"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.TrafficOnSpan

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">TrafficOnSpan</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Traffic information of a span along a route.

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

  `double`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-trafficonspan#baseSpeedInMetersPerSecond"
  class="member-name-link"><code>baseSpeedInMetersPerSecond</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The speed, in meters per second, without taking traffic into
  consideration.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-trafficonspan#consumptionInKilowattHours"
  class="member-name-link"><code>consumptionInKilowattHours</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The power consumption in kilowatt-hours (kWh) necessary to traverse
  the span.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-trafficonspan#duration"
  class="member-name-link"><code>duration</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The time duration necessary to traverse the traffic span.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-trafficonspan#incidentIndices"
  class="member-name-link"><code>incidentIndices</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The indices of traffic incidents from the field
  TrafficOnSection.trafficIncidents .

  </div>

  </div>

  <div class="col-first even-row-color">

  `double`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-trafficonspan#jamFactor"
  class="member-name-link"><code>jamFactor</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The traffic jam factor shows the traffic condition in a numeric way.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-trafficonspan#lengthInMeters"
  class="member-name-link"><code>lengthInMeters</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Length of the traffic span, in meters.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-trafficonspan#trafficDelay"
  class="member-name-link"><code>trafficDelay</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The estimated extra time in seconds spent due to traffic delays along
  this traffic span.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `int`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-trafficonspan#trafficSectionPolylineOffset"
  class="member-name-link"><code>trafficSectionPolylineOffset</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Index over TrafficOnSection.geometry where this span starts.

  </div>

  </div>

  <div class="col-first even-row-color">

  `double`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-trafficonspan#trafficSpeedInMetersPerSecond"
  class="member-name-link"><code>trafficSpeedInMetersPerSecond</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The speed, in meters per second, considering traffic.

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

      TrafficOnSpan()

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
<div id="sdk-for-android-explore-field-detail"
  class="section field-details">
<div id="sdk-for-android-explore-trafficSectionPolylineOffset"
    class="section detail">

    ### trafficSectionPolylineOffset

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">trafficSectionPolylineOffset</span>

    </div>

    <div class="block">

    Index over TrafficOnSection.geometry where this span starts.

    </div>

    </div>
<div id="sdk-for-android-explore-lengthInMeters"
    class="section detail">

    ### lengthInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">lengthInMeters</span>

    </div>

    <div class="block">

    Length of the traffic span, in meters.

    </div>

    </div>
<div id="sdk-for-android-explore-duration" class="section detail">

    ### duration

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">duration</span>

    </div>

    <div class="block">

    The time duration necessary to traverse the traffic span. This
    duration takes also into consideration the delays caused by the
    traffic.

    </div>

    </div>
<div id="sdk-for-android-explore-trafficDelay"
    class="section detail">

    ### trafficDelay

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">trafficDelay</span>

    </div>

    <div class="block">

    The estimated extra time in seconds spent due to traffic delays
    along this traffic span. Negative values indicate that the traffic
    span can be traversed faster than usual.

    </div>

    </div>
<div id="sdk-for-android-explore-baseSpeedInMetersPerSecond"
    class="section detail">

    ### baseSpeedInMetersPerSecond

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">baseSpeedInMetersPerSecond</span>

    </div>

    <div class="block">

    The speed, in meters per second, without taking traffic into
    consideration.

    </div>

    </div>
<div id="sdk-for-android-explore-trafficSpeedInMetersPerSecond"
    class="section detail">

    ### trafficSpeedInMetersPerSecond

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">trafficSpeedInMetersPerSecond</span>

    </div>

    <div class="block">

    The speed, in meters per second, considering traffic.

    </div>

    </div>
<div id="sdk-for-android-explore-jamFactor" class="section detail">

    ### jamFactor

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">jamFactor</span>

    </div>

    <div class="block">

    The traffic jam factor shows the traffic condition in a numeric way.
    It is a value in the range \[0.0, 10.0\]. A large jamFactor value
    means more traffic jam in general. Specifically, 0.0 means free
    traffic and 10.0 means stationary traffic.

    </div>

    </div>
<div id="sdk-for-android-explore-incidentIndices"
    class="section detail">

    ### incidentIndices

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a>></span> <span class="element-name">incidentIndices</span>

    </div>

    <div class="block">

    The indices of traffic incidents from the field
    TrafficOnSection.trafficIncidents .

    </div>

    </div>
<div id="sdk-for-android-explore-consumptionInKilowattHours"
    class="section detail">

    ### consumptionInKilowattHours

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">consumptionInKilowattHours</span>

    </div>

    <div class="block">

    The power consumption in kilowatt-hours (kWh) necessary to traverse
    the span.

    </div>

    </div>

  </div>
<div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">
<div id="sdk-for-android-explore-<init>()" class="section detail">

    ### TrafficOnSpan

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TrafficOnSpan</span>()

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
<div id="sdk-for-android-explore-hashCode()" class="section detail">

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

