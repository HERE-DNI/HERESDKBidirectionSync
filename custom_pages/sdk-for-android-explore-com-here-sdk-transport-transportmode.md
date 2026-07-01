---
title: "TransportMode (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-transport-transportmode"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.transport](sdk-for-android-explore-com-here-sdk-transport-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
java.lang.Enum<TransportMode>com.here.sdk.transport.TransportMode →
java.lang.Enum → TransportMode → com.here.sdk.transport.TransportMode

</div>

<div id="class-description" class="section class-description">

All Implemented Interfaces:  
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html"
class="external-link"
title="class or interface in java.io"><code>Serializable</code></a>, <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html"
class="external-link"
title="class or interface in java.lang"><code>Comparable</code></a>`<`[`TransportMode`](sdk-for-android-explore-com-here-sdk-transport-transportmode "enum class in com.here.sdk.transport")`>`,
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html"
class="external-link"
title="class or interface in java.lang.constant"><code>Constable</code></a>

<div class="type-signature">

<span class="modifiers">public enum
</span><span class="element-name type-name-label">TransportMode</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
class="external-link" title="class or interface in java.lang">Enum</a><[TransportMode](sdk-for-android-explore-com-here-sdk-transport-transportmode "enum class in com.here.sdk.transport")></span>

</div>

<div class="block">

Specifies the mode of transport used for route calculalation.

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="inherited-list">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>Enum.EnumDesc</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>E</code></a>` extends `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
  class="external-link"
  title="class or interface in java.lang"><code>Enum</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>E</code></a>`>>`

  </div>

  </div>

- <div id="enum-constant-summary" class="section constants-summary">

  <div class="caption">

  Enum Constants

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Enum Constant</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportmode#BICYCLE"
  class="member-name-link"><code>BICYCLE</code></a></td>
  <td><div class="block">
  Route calculation for bicycles.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportmode#BUS"
  class="member-name-link"><code>BUS</code></a></td>
  <td><div class="block">
  Route calculation for buses.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportmode#CAR"
  class="member-name-link"><code>CAR</code></a></td>
  <td><div class="block">
  The calculated route is optimized for cars.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportmode#PEDESTRIAN"
  class="member-name-link"><code>PEDESTRIAN</code></a></td>
  <td><div class="block">
  The calculated route is optimized for pedestrians.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportmode#PRIVATE_BUS"
  class="member-name-link"><code>PRIVATE_BUS</code></a></td>
  <td><div class="block">
  Route calculation for private buses.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportmode#PUBLIC_TRANSIT"
  class="member-name-link"><code>PUBLIC_TRANSIT</code></a></td>
  <td><div class="block">
  The calculated route is optimized for public transit.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportmode#SCOOTER"
  class="member-name-link"><code>SCOOTER</code></a></td>
  <td><div class="block">
  The calculated route is optimized for scooters.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportmode#TAXI"
  class="member-name-link"><code>TAXI</code></a></td>
  <td><div class="block">
  The taxi transport mode takes into account tax restricted streets as
  well as streets reserved for exclusive taxi access.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportmode#TRUCK"
  class="member-name-link"><code>TRUCK</code></a></td>
  <td><div class="block">
  The calculated route is optimized for trucks.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Static Methods
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
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportmode"
  title="enum class in com.here.sdk.transport"><code>TransportMode</code></a></td>
  <td><pre><code>valueOf(String name)</code></pre></td>
  <td><div class="block">
  Returns the enum constant of this class with the specified name.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-transport-transportmode"
  title="enum class in com.here.sdk.transport"><code>TransportMode</code></a><code>[]</code></td>
  <td><pre><code>values()</code></pre></td>
  <td><div class="block">
  Returns an array containing the constants of this enum class, in the
  order they are declared.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
  class="external-link" title="class or interface in java.lang">Enum</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)"
  class="external-link"
  title="class or interface in java.lang"><code>compareTo</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()"
  class="external-link"
  title="class or interface in java.lang"><code>describeConstable</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getDeclaringClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()"
  class="external-link"
  title="class or interface in java.lang"><code>name</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()"
  class="external-link"
  title="class or interface in java.lang"><code>ordinal</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)"
  class="external-link"
  title="class or interface in java.lang"><code>valueOf</code></a>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
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

- <div id="enum-constant-detail" class="section constant-details">

  - <div id="CAR" class="section detail">

    ### CAR

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TransportMode](sdk-for-android-explore-com-here-sdk-transport-transportmode "enum class in com.here.sdk.transport")</span> <span class="element-name">CAR</span>

    </div>

    <div class="block">

    The calculated route is optimized for cars.

    </div>

    </div>

  - <div id="TRUCK" class="section detail">

    ### TRUCK

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TransportMode](sdk-for-android-explore-com-here-sdk-transport-transportmode "enum class in com.here.sdk.transport")</span> <span class="element-name">TRUCK</span>

    </div>

    <div class="block">

    The calculated route is optimized for trucks. This mode considers
    truck restrictions and uses truck specific speed assumptions when
    calculating the route.

    </div>

    </div>

  - <div id="PEDESTRIAN" class="section detail">

    ### PEDESTRIAN

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TransportMode](sdk-for-android-explore-com-here-sdk-transport-transportmode "enum class in com.here.sdk.transport")</span> <span class="element-name">PEDESTRIAN</span>

    </div>

    <div class="block">

    The calculated route is optimized for pedestrians. As one effect,
    maneuvers will be optimized for walking, i.e. segments will consider
    actions relevant for pedestrians and maneuver instructions will
    contain texts suitable for a walking person. This mode disregards
    any traffic information.

    </div>

    </div>

  - <div id="SCOOTER" class="section detail">

    ### SCOOTER

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TransportMode](sdk-for-android-explore-com-here-sdk-transport-transportmode "enum class in com.here.sdk.transport")</span> <span class="element-name">SCOOTER</span>

    </div>

    <div class="block">

    The calculated route is optimized for scooters.

    </div>

    </div>

  - <div id="BICYCLE" class="section detail">

    ### BICYCLE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TransportMode](sdk-for-android-explore-com-here-sdk-transport-transportmode "enum class in com.here.sdk.transport")</span> <span class="element-name">BICYCLE</span>

    </div>

    <div class="block">

    Route calculation for bicycles.

    </div>

    </div>

  - <div id="PUBLIC_TRANSIT" class="section detail">

    ### PUBLIC_TRANSIT

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TransportMode](sdk-for-android-explore-com-here-sdk-transport-transportmode "enum class in com.here.sdk.transport")</span> <span class="element-name">PUBLIC_TRANSIT</span>

    </div>

    <div class="block">

    The calculated route is optimized for public transit. Note that this
    transport mode is available only for some versions of the HERE SDK.
    Check SDKBuildInformation and consult your HERE representative if
    necessary.

    </div>

    </div>

  - <div id="TAXI" class="section detail">

    ### TAXI

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TransportMode](sdk-for-android-explore-com-here-sdk-transport-transportmode "enum class in com.here.sdk.transport")</span> <span class="element-name">TAXI</span>

    </div>

    <div class="block">

    The taxi transport mode takes into account tax restricted streets as
    well as streets reserved for exclusive taxi access. Note that roads
    that are restricted or reserved for taxis are avoided, unless a
    waypoint is set on such a road - as this may indicate to pick-up or
    to drop-off a passenger. Note: This is a beta release of this
    transport mode, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases or even become
    unsupported, without a deprecation process.

    </div>

    </div>

  - <div id="BUS" class="section detail">

    ### BUS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TransportMode](sdk-for-android-explore-com-here-sdk-transport-transportmode "enum class in com.here.sdk.transport")</span> <span class="element-name">BUS</span>

    </div>

    <div class="block">

    Route calculation for buses. Denotes those vehicles operated by
    public transport provider. This transport mode has the access to the
    bus-only lane/road.

    </div>

    </div>

  - <div id="PRIVATE_BUS" class="section detail">

    ### PRIVATE_BUS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[TransportMode](sdk-for-android-explore-com-here-sdk-transport-transportmode "enum class in com.here.sdk.transport")</span> <span class="element-name">PRIVATE_BUS</span>

    </div>

    <div class="block">

    Route calculation for private buses. Denotes those vehicles operated
    by private transport company. This transport mode does not have the
    access to the bus-only lane/road.

    </div>

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="values()" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[TransportMode](sdk-for-android-explore-com-here-sdk-transport-transportmode "enum class in com.here.sdk.transport")\[\]</span> <span class="element-name">values</span>()

    </div>

    <div class="block">

    Returns an array containing the constants of this enum class, in the
    order they are declared.

    </div>

    Returns:  
    an array containing the constants of this enum class, in the order
    they are declared

    </div>

  - <div id="valueOf(java.lang.String)" class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[TransportMode](sdk-for-android-explore-com-here-sdk-transport-transportmode "enum class in com.here.sdk.transport")</span> <span class="element-name">valueOf</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Returns the enum constant of this class with the specified name. The
    string must match exactly an identifier used to declare an enum
    constant in this class. (Extraneous whitespace characters are not
    permitted.)

    </div>

    Parameters:  
    `name` - the name of the enum constant to be returned.

    Returns:  
    the enum constant with the specified name

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalArgumentException</code></a> -
    if this enum class has no constant with the specified name

    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html"
    class="external-link"
    title="class or interface in java.lang"><code>NullPointerException</code></a> -
    if the argument is null

    </div>

  </div>

</div>

