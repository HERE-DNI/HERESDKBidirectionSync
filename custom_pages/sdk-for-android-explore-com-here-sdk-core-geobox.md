---
title: "GeoBox (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-geobox"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.core.GeoBox

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">GeoBox</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents a bounding rectangle aligned with latitude and longitude.
Geographic area represented by this would be visualised as a rectangle
when using a normal cylindrical projection (such as Mercator). The box
has a maximum span of 360 degrees in longitude and 180 degrees in
latitude direction. The box with equal values in longitude for the
corners is considered as a span of 360 degrees. The box is considered
empty if the latitude of the southWestCorner is larger than the the
latitude of the northEastCorner .

</div>

</div>

<div class="section summary">

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
  <td><code>final </code><a
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-geobox#northEastCorner"
  class="member-name-link"><code>northEastCorner</code></a></td>
  <td><div class="block">
  North east corner coordinates.
  </div></td>
  </tr>
  <tr>
  <td><code>final </code><a
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-geobox#southWestCorner"
  class="member-name-link"><code>southWestCorner</code></a></td>
  <td><div class="block">
  South west corner coordinates.
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
  <td><pre><code>GeoBox(GeoCoordinates southWestCorner,
   GeoCoordinates northEastCorner)</code></pre></td>
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
  Static Methods
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
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-core-geobox"
  title="class in com.here.sdk.core"><code>GeoBox</code></a></td>
  <td><pre><code>containing(List&lt;GeoCoordinates&gt; geoCoordinates)</code></pre></td>
  <td><div class="block">
  Creates a GeoBox which encompases all coordinates from the list.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>contains(GeoBox geoBox)</code></pre></td>
  <td><div class="block">
  Determines whether the specified GeoBox is covered entirely by this
  GeoBox .
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>contains(GeoCoordinates geoCoordinates)</code></pre></td>
  <td><div class="block">
  Determines whether the specified GeoCoordinates is contained within this
  GeoBox .
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geobox"
  title="class in com.here.sdk.core"><code>GeoBox</code></a></td>
  <td><pre><code>envelope(GeoBox geoBox)</code></pre></td>
  <td><div class="block">
  Envelopes two GeoBox areas by returning the smallest GeoBox covering
  both this GeoBox and the specified GeoBox .
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-core-geobox"
  title="class in com.here.sdk.core"><code>GeoBox</code></a></td>
  <td><pre><code>envelopeGeoBoxes(List&lt;GeoBox&gt; geoBoxes)</code></pre></td>
  <td><div class="block">
  Envelopes the list of GeoBox areas by returning the smallest GeoBox
  covering all specified GeoBox objects.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>equals(Object obj)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geobox"
  title="class in com.here.sdk.core"><code>GeoBox</code></a></td>
  <td><pre><code>expandedBy(double southMeters,
   double westMeters,
   double northMeters,
   double eastMeters)</code></pre></td>
  <td><div class="block">
  Creates a GeoBox which is expanded by a fixed distance.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-core-geobox"
  title="class in com.here.sdk.core"><code>GeoBox</code></a><code>&gt;</code></td>
  <td><pre><code>intersection(GeoBox geoBox)</code></pre></td>
  <td><div class="block">
  Computes the intersection with the passed GeoBox .
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-core-geobox"
  title="class in com.here.sdk.core"><code>GeoBox</code></a><code>&gt;</code></td>
  <td><pre><code>intersection(List&lt;GeoBox&gt; geoBoxes)</code></pre></td>
  <td><div class="block">
  Computes intersection of list of GeoBox instances.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>intersects(GeoBox geoBox)</code></pre></td>
  <td><div class="block">
  Determines whether this GeoBox intersects with the passed GeoBox .
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

  - <div id="southWestCorner" class="section detail">

    ### southWestCorner

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    final</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">southWestCorner</span>

    </div>

    <div class="block">

    South west corner coordinates.

    </div>

    </div>

  - <div id="northEastCorner" class="section detail">

    ### northEastCorner

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    final</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">northEastCorner</span>

    </div>

    <div class="block">

    North east corner coordinates.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### GeoBox

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoBox</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") southWestCorner,
    @NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") northEastCorner)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `southWestCorner` -

    South west corner coordinates.

    `northEastCorner` -

    North east corner coordinates.

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

  - <div id="containing(java.util.List)" class="section detail">

    ### containing

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public
    static</span> <span class="return-type">[GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")</span> <span class="element-name">containing</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")> geoCoordinates)</span>

    </div>

    <div class="block">

    Creates a GeoBox which encompases all coordinates from the list. The
    provided list must contain at least two points. The altitude values
    of the input coordinates are not considered for the result.

    </div>

    Parameters:  
    `geoCoordinates` -

    List of coordinates to encompass inside bounding box.

    Returns:  
    `GeoBox` containing all supplied coordinates, or `null` if less than
    two coordinates were provided.

    </div>

  - <div id="envelope(com.here.sdk.core.GeoBox)" class="section detail">

    ### envelope

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")</span> <span class="element-name">envelope</span><span class="parameters">(@NonNull
    [GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core") geoBox)</span>

    </div>

    <div class="block">

    Envelopes two GeoBox areas by returning the smallest GeoBox covering
    both this GeoBox and the specified GeoBox .

    </div>

    Parameters:  
    `geoBox` -

    Another `GeoBox` to envelope with.

    Returns:  
    `GeoBox` covering two`GeoBox` areas

    </div>

  - <div id="envelopeGeoBoxes(java.util.List)" class="section detail">

    ### envelopeGeoBoxes

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public
    static</span> <span class="return-type">[GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")</span> <span class="element-name">envelopeGeoBoxes</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")> geoBoxes)</span>

    </div>

    <div class="block">

    Envelopes the list of GeoBox areas by returning the smallest GeoBox
    covering all specified GeoBox objects.

    </div>

    Parameters:  
    `geoBoxes` -

    List of `GeoBox` objects.

    Returns:  
    `GeoBox` covering all `GeoBox` areas, or `null` if input is empty.

    </div>

  - <div id="intersects(com.here.sdk.core.GeoBox)"
    class="section detail">

    ### intersects

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">intersects</span><span class="parameters">(@NonNull
    [GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core") geoBox)</span>

    </div>

    <div class="block">

    Determines whether this GeoBox intersects with the passed GeoBox .
    The altitude values are ignored.

    </div>

    Parameters:  
    `geoBox` -

    A `GeoBox` to check for intersection.

    Returns:  
    `true` if intersects with the `GeoBox`, `false` otherwise.

    </div>

  - <div id="intersection(com.here.sdk.core.GeoBox)"
    class="section detail">

    ### intersection

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")></span> <span class="element-name">intersection</span><span class="parameters">(@NonNull
    [GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core") geoBox)</span>

    </div>

    <div class="block">

    Computes the intersection with the passed GeoBox . The altitude
    values are ignored. Limitation: Geo boxes are considered as
    non-intersecting if they overlap only on a single point, horizontal
    line or vertical line. Note: This is a beta release of this feature,
    so there could be a few bugs and unexpected behaviors. Related APIs
    may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `geoBox` -

    Another geo box to check intersection with.

    Returns:  
    It will be empty if there is no overlap. Otherwise, 1 or more geo
    boxes covering common area by this and passed
    [`GeoBox`](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core").

    </div>

  - <div id="intersection(java.util.List)" class="section detail">

    ### intersection

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")></span> <span class="element-name">intersection</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")> geoBoxes)</span>

    </div>

    <div class="block">

    Computes intersection of list of GeoBox instances. The altitude
    values are ignored. Limitation: Geo boxes are considered as
    non-intersecting if they overlap only on a single point, horizontal
    line or vertical line. Note: This is a beta release of this feature,
    so there could be a few bugs and unexpected behaviors. Related APIs
    may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `geoBoxes` -

    List of
    [`GeoBox`](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")
    instances.

    Returns:  
    It will be empty if there is no overlap between all the passed
    [`GeoBox`](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")
    instances. Otherwise, 1 or more geo boxes covering common area by
    all the passed
    [`GeoBox`](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")
    instances.

    </div>

  - <div id="contains(com.here.sdk.core.GeoBox)" class="section detail">

    ### contains

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">contains</span><span class="parameters">(@NonNull
    [GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core") geoBox)</span>

    </div>

    <div class="block">

    Determines whether the specified GeoBox is covered entirely by this
    GeoBox . The altitude values are ignored.

    </div>

    Parameters:  
    `geoBox` -

    A `GeoBox` to check for containment within this `GeoBox`.

    Returns:  
    `true` if covered by the `GeoBox`, `false` otherwise.

    </div>

  - <div id="contains(com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### contains

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">contains</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") geoCoordinates)</span>

    </div>

    <div class="block">

    Determines whether the specified GeoCoordinates is contained within
    this GeoBox . The altitude values are ignored.

    </div>

    Parameters:  
    `geoCoordinates` -

    A GeoCoordinates to check for containment within this `GeoBox`.

    Returns:  
    `true` if contained within the `GeoBox`, `false` otherwise.

    </div>

  - <div id="expandedBy(double,double,double,double)"
    class="section detail">

    ### expandedBy

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")</span> <span class="element-name">expandedBy</span><span class="parameters">(double southMeters,
    double westMeters, double northMeters, double eastMeters)</span>
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a GeoBox which is expanded by a fixed distance. Throws an
    InstantiationError if it is not possible to create a valid GeoBox
    with the given arguments.

    </div>

    Parameters:  
    `southMeters` -

    Distance in the south direction in meters to expand the `GeoBox`.

    `westMeters` -

    Distance in the west direction in meters to expand the `GeoBox`.

    `northMeters` -

    Distance in the north direction in meters to expand the `GeoBox`.

    `eastMeters` -

    Distance in the east direction in meters to expand the `GeoBox`.

    Returns:  
    The expanded `GeoBox`.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")
    -

    Instantiation error.

    </div>

  </div>

</div>

