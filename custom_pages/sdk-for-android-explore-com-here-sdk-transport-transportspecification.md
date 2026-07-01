---
title: "TransportSpecification (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-transport-transportspecification"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.transport](sdk-for-android-explore-com-here-sdk-transport-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.transport.TransportSpecification

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">TransportSpecification</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Contains transport attributes details related to the transport mode.
Notes By default all vehicle specifications from
RoutingOptions.transport_specification are set to null and the
RoutingOptions.transport_specification.transport_mode is set to
TransportMode.CAR . A route can be calculated with only the
RoutingOptions.transport_specification.transport_mode set.

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportspecification-bicyclebuilder"
  class="type-name-link"
  title="class in com.here.sdk.transport"><code>TransportSpecification.BicycleBuilder</code></a></td>
  <td><div class="block">
  This class constructs a TransportSpecification for a bicycle.
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportspecification-busbuilder"
  class="type-name-link"
  title="class in com.here.sdk.transport"><code>TransportSpecification.BusBuilder</code></a></td>
  <td><div class="block">
  This class constructs a TransportSpecification for a bus.
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportspecification-carbuilder"
  class="type-name-link"
  title="class in com.here.sdk.transport"><code>TransportSpecification.CarBuilder</code></a></td>
  <td><div class="block">
  This class constructs a TransportSpecification for a car.
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportspecification-pedestrianbuilder"
  class="type-name-link"
  title="class in com.here.sdk.transport"><code>TransportSpecification.PedestrianBuilder</code></a></td>
  <td><div class="block">
  This class constructs a TransportSpecification for pedestrian.
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportspecification-privatebusbuilder"
  class="type-name-link"
  title="class in com.here.sdk.transport"><code>TransportSpecification.PrivateBusBuilder</code></a></td>
  <td><div class="block">
  This class constructs a TransportSpecification for a private bus.
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportspecification-scooterbuilder"
  class="type-name-link"
  title="class in com.here.sdk.transport"><code>TransportSpecification.ScooterBuilder</code></a></td>
  <td><div class="block">
  This class constructs a TransportSpecification for a scooter.
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportspecification-taxibuilder"
  class="type-name-link"
  title="class in com.here.sdk.transport"><code>TransportSpecification.TaxiBuilder</code></a></td>
  <td><div class="block">
  This class constructs a TransportSpecification for a taxi.
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportspecification-truckbuilder"
  class="type-name-link"
  title="class in com.here.sdk.transport"><code>TransportSpecification.TruckBuilder</code></a></td>
  <td><div class="block">
  This class constructs a TransportSpecification for a truck.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Field</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-pedestrianspecification"
  title="class in com.here.sdk.transport"><code>PedestrianSpecification</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportspecification#pedestrianSpecification"
  class="member-name-link"><code>pedestrianSpecification</code></a></td>
  <td><div class="block">
  The pedestrian specification for the transport mode.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-scooterspecification"
  title="class in com.here.sdk.transport"><code>ScooterSpecification</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportspecification#scooterSpecification"
  class="member-name-link"><code>scooterSpecification</code></a></td>
  <td><div class="block">
  The scooter specification for the transport mode.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-taxispecification"
  title="class in com.here.sdk.transport"><code>TaxiSpecification</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportspecification#taxiSpecification"
  class="member-name-link"><code>taxiSpecification</code></a></td>
  <td><div class="block">
  The taxi specification for the transport mode.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportmode"
  title="enum class in com.here.sdk.transport"><code>TransportMode</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportspecification#transportMode"
  class="member-name-link"><code>transportMode</code></a></td>
  <td><div class="block">
  Transport mode.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-vehiclespecification"
  title="class in com.here.sdk.transport"><code>VehicleSpecification</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportspecification#vehicleSpecification"
  class="member-name-link"><code>vehicleSpecification</code></a></td>
  <td><div class="block">
  The vehicle specification for the transport mode.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Constructor</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><pre><code>TransportSpecification()</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

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
  <td><code>boolean</code></td>
  <td><pre><code>equals(Object obj)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
  <td> </td>
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

- <div id="field-detail" class="section field-details">

  - <div id="transportMode" class="section detail">

    ### transportMode

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TransportMode](sdk-for-android-explore-com-here-sdk-transport-transportmode "enum class in com.here.sdk.transport")</span> <span class="element-name">transportMode</span>

    </div>

    <div class="block">

    Transport mode. Defaults to CAR .

    </div>

    </div>

  - <div id="vehicleSpecification" class="section detail">

    ### vehicleSpecification

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[VehicleSpecification](sdk-for-android-explore-com-here-sdk-transport-vehiclespecification "class in com.here.sdk.transport")</span> <span class="element-name">vehicleSpecification</span>

    </div>

    <div class="block">

    The vehicle specification for the transport mode. By default, it is
    not set.

    </div>

    </div>

  - <div id="pedestrianSpecification" class="section detail">

    ### pedestrianSpecification

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[PedestrianSpecification](sdk-for-android-explore-com-here-sdk-transport-pedestrianspecification "class in com.here.sdk.transport")</span> <span class="element-name">pedestrianSpecification</span>

    </div>

    <div class="block">

    The pedestrian specification for the transport mode. By default, it
    is not set.

    </div>

    </div>

  - <div id="taxiSpecification" class="section detail">

    ### taxiSpecification

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[TaxiSpecification](sdk-for-android-explore-com-here-sdk-transport-taxispecification "class in com.here.sdk.transport")</span> <span class="element-name">taxiSpecification</span>

    </div>

    <div class="block">

    The taxi specification for the transport mode. By default, it is not
    set.

    </div>

    </div>

  - <div id="scooterSpecification" class="section detail">

    ### scooterSpecification

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[ScooterSpecification](sdk-for-android-explore-com-here-sdk-transport-scooterspecification "class in com.here.sdk.transport")</span> <span class="element-name">scooterSpecification</span>

    </div>

    <div class="block">

    The scooter specification for the transport mode. By default, it is
    not set.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### TransportSpecification

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TransportSpecification</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="equals(java.lang.Object)" class="section detail">

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

  - <div id="hashCode()" class="section detail">

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

