---
title: "SegmentReference (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-segmentreference"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.SegmentReference

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">SegmentReference</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Reference to a segment id with a travel direction. Note: This is a beta
release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a
deprecation process.

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
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html"
  class="external-link"
  title="class or interface in java.lang"><code>Long</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-segmentreference#localId"
  class="member-name-link"><code>localId</code></a></td>
  <td><div class="block">
  Local ID of the segment inside the OCM tile.
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-segmentreference#offsetEnd"
  class="member-name-link"><code>offsetEnd</code></a></td>
  <td><div class="block">
  The end offset is a non-negative number between 0 and 1, representing
  the end of the referenced range using a proportion of the length of the
  segment.
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-segmentreference#offsetStart"
  class="member-name-link"><code>offsetStart</code></a></td>
  <td><div class="block">
  The start offset is a non-negative number between 0 and 1, representing
  the start of the referenced range using a proportion of the length of
  the segment.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-segmentreference#segmentId"
  class="member-name-link"><code>segmentId</code></a></td>
  <td><div class="block">
  Topology segment id representing a unique identifier within the HERE
  platform catalogs.
  </div></td>
  </tr>
  <tr>
  <td><code>long</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-segmentreference#tilePartitionId"
  class="member-name-link"><code>tilePartitionId</code></a></td>
  <td><div class="block">
  HERE tile partition id (Morton-encoding + level indicator) of the
  segment.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-traveldirection"
  title="enum class in com.here.sdk.routing"><code>TravelDirection</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-segmentreference#travelDirection"
  class="member-name-link"><code>travelDirection</code></a></td>
  <td><div class="block">
  Travel direction of the segment.
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
  <td><pre><code>SegmentReference()</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>SegmentReference(String segmentId)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>SegmentReference(String segmentId,
   TravelDirection travelDirection)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>SegmentReference(String segmentId,
   TravelDirection travelDirection,
   double offsetStart)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>SegmentReference(String segmentId,
   TravelDirection travelDirection,
   double offsetStart,
   double offsetEnd)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>SegmentReference(String segmentId,
   TravelDirection travelDirection,
   double offsetStart,
   double offsetEnd,
   long tilePartitionId)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>SegmentReference(String segmentId,
   TravelDirection travelDirection,
   double offsetStart,
   double offsetEnd,
   long tilePartitionId,
   Long localId)</code></pre></td>
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
  <td><code>boolean</code></td>
  <td><pre><code>equals(Object obj)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-routing-segmentreference"
  title="class in com.here.sdk.routing"><code>SegmentReference</code></a></td>
  <td><pre><code>fromString(String segmentRef)</code></pre></td>
  <td><div class="block">
  Returns an instance of this struct from a string if it's well-formatted,
  null otherwise.
  </div></td>
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

  - <div id="segmentId" class="section detail">

    ### segmentId

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">segmentId</span>

    </div>

    <div class="block">

    Topology segment id representing a unique identifier within the HERE
    platform catalogs.

    </div>

    </div>

  - <div id="travelDirection" class="section detail">

    ### travelDirection

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TravelDirection](sdk-for-android-explore-com-here-sdk-routing-traveldirection "enum class in com.here.sdk.routing")</span> <span class="element-name">travelDirection</span>

    </div>

    <div class="block">

    Travel direction of the segment.

    </div>

    </div>

  - <div id="offsetStart" class="section detail">

    ### offsetStart

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">offsetStart</span>

    </div>

    <div class="block">

    The start offset is a non-negative number between 0 and 1,
    representing the start of the referenced range using a proportion of
    the length of the segment. 0 represents the start and 1 the end of
    the segment, relative to the indicated direction (or positive
    direction in case of undirected segments)

    </div>

    </div>

  - <div id="offsetEnd" class="section detail">

    ### offsetEnd

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">offsetEnd</span>

    </div>

    <div class="block">

    The end offset is a non-negative number between 0 and 1,
    representing the end of the referenced range using a proportion of
    the length of the segment. 0 represents the start and 1 the end of
    the segment, relative to the indicated direction (or positive
    direction in case of undirected segments)

    </div>

    </div>

  - <div id="tilePartitionId" class="section detail">

    ### tilePartitionId

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">tilePartitionId</span>

    </div>

    <div class="block">

    HERE tile partition id (Morton-encoding + level indicator) of the
    segment. As in HERE Map Content.

    </div>

    </div>

  - <div id="localId" class="section detail">

    ### localId

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html"
    class="external-link" title="class or interface in java.lang">Long</a></span> <span class="element-name">localId</span>

    </div>

    <div class="block">

    Local ID of the segment inside the OCM tile.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### SegmentReference

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SegmentReference</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  - <div id="<init>(java.lang.String)" class="section detail">

    ### SegmentReference

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SegmentReference</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> segmentId)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `segmentId` -

    Topology segment id representing a unique identifier within the HERE
    platform catalogs.

    </div>

  - <div id="<init>(java.lang.String,com.here.sdk.routing.TravelDirection)"
    class="section detail">

    ### SegmentReference

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SegmentReference</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> segmentId,
    @NonNull
    [TravelDirection](sdk-for-android-explore-com-here-sdk-routing-traveldirection "enum class in com.here.sdk.routing") travelDirection)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `segmentId` -

    Topology segment id representing a unique identifier within the HERE
    platform catalogs.

    `travelDirection` -

    Travel direction of the segment.

    </div>

  - <div id="<init>(java.lang.String,com.here.sdk.routing.TravelDirection,double)"
    class="section detail">

    ### SegmentReference

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SegmentReference</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> segmentId,
    @NonNull
    [TravelDirection](sdk-for-android-explore-com-here-sdk-routing-traveldirection "enum class in com.here.sdk.routing") travelDirection,
    double offsetStart)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `segmentId` -

    Topology segment id representing a unique identifier within the HERE
    platform catalogs.

    `travelDirection` -

    Travel direction of the segment.

    `offsetStart` -

    The start offset is a non-negative number between 0 and 1,
    representing the start of the referenced range using a proportion of
    the length of the segment. 0 represents the start and 1 the end of
    the segment, relative to the indicated direction (or positive
    direction in case of undirected segments)

    </div>

  - <div id="<init>(java.lang.String,com.here.sdk.routing.TravelDirection,double,double)"
    class="section detail">

    ### SegmentReference

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SegmentReference</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> segmentId,
    @NonNull
    [TravelDirection](sdk-for-android-explore-com-here-sdk-routing-traveldirection "enum class in com.here.sdk.routing") travelDirection,
    double offsetStart, double offsetEnd)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `segmentId` -

    Topology segment id representing a unique identifier within the HERE
    platform catalogs.

    `travelDirection` -

    Travel direction of the segment.

    `offsetStart` -

    The start offset is a non-negative number between 0 and 1,
    representing the start of the referenced range using a proportion of
    the length of the segment. 0 represents the start and 1 the end of
    the segment, relative to the indicated direction (or positive
    direction in case of undirected segments)

    `offsetEnd` -

    The end offset is a non-negative number between 0 and 1,
    representing the end of the referenced range using a proportion of
    the length of the segment. 0 represents the start and 1 the end of
    the segment, relative to the indicated direction (or positive
    direction in case of undirected segments)

    </div>

  - <div id="<init>(java.lang.String,com.here.sdk.routing.TravelDirection,double,double,long)"
    class="section detail">

    ### SegmentReference

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SegmentReference</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> segmentId,
    @NonNull
    [TravelDirection](sdk-for-android-explore-com-here-sdk-routing-traveldirection "enum class in com.here.sdk.routing") travelDirection,
    double offsetStart, double offsetEnd, long tilePartitionId)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `segmentId` -

    Topology segment id representing a unique identifier within the HERE
    platform catalogs.

    `travelDirection` -

    Travel direction of the segment.

    `offsetStart` -

    The start offset is a non-negative number between 0 and 1,
    representing the start of the referenced range using a proportion of
    the length of the segment. 0 represents the start and 1 the end of
    the segment, relative to the indicated direction (or positive
    direction in case of undirected segments)

    `offsetEnd` -

    The end offset is a non-negative number between 0 and 1,
    representing the end of the referenced range using a proportion of
    the length of the segment. 0 represents the start and 1 the end of
    the segment, relative to the indicated direction (or positive
    direction in case of undirected segments)

    `tilePartitionId` -

    HERE tile partition id (Morton-encoding + level indicator) of the
    segment. As in HERE Map Content.

    </div>

  - <div id="<init>(java.lang.String,com.here.sdk.routing.TravelDirection,double,double,long,java.lang.Long)"
    class="section detail">

    ### SegmentReference

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SegmentReference</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> segmentId,
    @NonNull
    [TravelDirection](sdk-for-android-explore-com-here-sdk-routing-traveldirection "enum class in com.here.sdk.routing") travelDirection,
    double offsetStart, double offsetEnd, long tilePartitionId,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html"
    class="external-link" title="class or interface in java.lang">Long</a> localId)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `segmentId` -

    Topology segment id representing a unique identifier within the HERE
    platform catalogs.

    `travelDirection` -

    Travel direction of the segment.

    `offsetStart` -

    The start offset is a non-negative number between 0 and 1,
    representing the start of the referenced range using a proportion of
    the length of the segment. 0 represents the start and 1 the end of
    the segment, relative to the indicated direction (or positive
    direction in case of undirected segments)

    `offsetEnd` -

    The end offset is a non-negative number between 0 and 1,
    representing the end of the referenced range using a proportion of
    the length of the segment. 0 represents the start and 1 the end of
    the segment, relative to the indicated direction (or positive
    direction in case of undirected segments)

    `tilePartitionId` -

    HERE tile partition id (Morton-encoding + level indicator) of the
    segment. As in HERE Map Content.

    `localId` -

    Local ID of the segment inside the OCM tile.

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

  - <div id="fromString(java.lang.String)" class="section detail">

    ### fromString

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public
    static</span> <span class="return-type">[SegmentReference](sdk-for-android-explore-com-here-sdk-routing-segmentreference "class in com.here.sdk.routing")</span> <span class="element-name">fromString</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> segmentRef)</span>

    </div>

    <div class="block">

    Returns an instance of this struct from a string if it's
    well-formatted, null otherwise.

    </div>

    Parameters:  
    `segmentRef` -

    The string to parse

    Returns:  
    An instance of
    [`SegmentReference`](sdk-for-android-explore-com-here-sdk-routing-segmentreference "class in com.here.sdk.routing")
    from a string if it's well-formatted, `null` otherwise.

    </div>

  </div>

</div>

