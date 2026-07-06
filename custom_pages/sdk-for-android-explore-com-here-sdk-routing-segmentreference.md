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

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">SegmentReference</span>
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Reference to a segment id with a travel direction. Note: This is a beta
release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a
deprecation process.

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" class="external-link" title="class or interface in java.lang"><code>Long</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-segmentreference#localId" class="member-name-link"><code>localId</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Local ID of the segment inside the OCM tile.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-segmentreference#offsetEnd" class="member-name-link"><code>offsetEnd</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The end offset is a non-negative number between 0 and 1, representing
  the end of the referenced range using a proportion of the length of
  the segment.

  </div>

  </div>

  <div class="col-first even-row-color">

  `double`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-segmentreference#offsetStart" class="member-name-link"><code>offsetStart</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The start offset is a non-negative number between 0 and 1,
  representing the start of the referenced range using a proportion of
  the length of the segment.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-segmentreference#segmentId" class="member-name-link"><code>segmentId</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Topology segment id representing a unique identifier within the HERE
  platform catalogs.

  </div>

  </div>

  <div class="col-first even-row-color">

  `long`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-segmentreference#tilePartitionId" class="member-name-link"><code>tilePartitionId</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  HERE tile partition id (Morton-encoding + level indicator) of the
  segment.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`TravelDirection`](sdk-for-android-explore-com-here-sdk-routing-traveldirection "enum class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-segmentreference#travelDirection" class="member-name-link"><code>travelDirection</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Travel direction of the segment.

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

      SegmentReference()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      SegmentReference(String segmentId)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      SegmentReference(String segmentId,
       TravelDirection travelDirection)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      SegmentReference(String segmentId,
       TravelDirection travelDirection,
       double offsetStart)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      SegmentReference(String segmentId,
       TravelDirection travelDirection,
       double offsetStart,
       double offsetEnd)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      SegmentReference(String segmentId,
       TravelDirection travelDirection,
       double offsetStart,
       double offsetEnd,
       long tilePartitionId)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      SegmentReference(String segmentId,
       TravelDirection travelDirection,
       double offsetStart,
       double offsetEnd,
       long tilePartitionId,
       Long localId)

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

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`SegmentReference`](sdk-for-android-explore-com-here-sdk-routing-segmentreference "class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      fromString(String segmentRef)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns an instance of this struct from a string if it's
  well-formatted, null otherwise.

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

- <div id="sdk-for-android-explore-field-detail"
  class="section field-details">

  - <div id="sdk-for-android-explore-segmentId" class="section detail">

    ### segmentId

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">segmentId</span>

    </div>

    <div class="block">

    Topology segment id representing a unique identifier within the HERE
    platform catalogs.

    </div>

    </div>

  - <div id="sdk-for-android-explore-travelDirection"
    class="section detail">

    ### travelDirection

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TravelDirection](sdk-for-android-explore-com-here-sdk-routing-traveldirection "enum class in com.here.sdk.routing")</span> <span class="element-name">travelDirection</span>

    </div>

    <div class="block">

    Travel direction of the segment.

    </div>

    </div>

  - <div id="sdk-for-android-explore-offsetStart"
    class="section detail">

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

  - <div id="sdk-for-android-explore-offsetEnd" class="section detail">

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

  - <div id="sdk-for-android-explore-tilePartitionId"
    class="section detail">

    ### tilePartitionId

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">tilePartitionId</span>

    </div>

    <div class="block">

    HERE tile partition id (Morton-encoding + level indicator) of the
    segment. As in HERE Map Content.

    </div>

    </div>

  - <div id="sdk-for-android-explore-localId" class="section detail">

    ### localId

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" class="external-link" title="class or interface in java.lang">Long</a></span> <span class="element-name">localId</span>

    </div>

    <div class="block">

    Local ID of the segment inside the OCM tile.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>()" class="section detail">

    ### SegmentReference

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SegmentReference</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  - <div id="sdk-for-android-explore-<init>(java.lang.String)"
    class="section detail">

    ### SegmentReference

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SegmentReference</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> segmentId)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `segmentId` -

    Topology segment id representing a unique identifier within the HERE
    platform catalogs.

    </div>

  - <div id="sdk-for-android-explore-<init>(java.lang.String,com.here.sdk.routing.TravelDirection)"
    class="section detail">

    ### SegmentReference

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SegmentReference</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> segmentId,
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

  - <div id="sdk-for-android-explore-<init>(java.lang.String,com.here.sdk.routing.TravelDirection,double)"
    class="section detail">

    ### SegmentReference

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SegmentReference</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> segmentId,
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

  - <div id="sdk-for-android-explore-<init>(java.lang.String,com.here.sdk.routing.TravelDirection,double,double)"
    class="section detail">

    ### SegmentReference

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SegmentReference</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> segmentId,
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

  - <div id="sdk-for-android-explore-<init>(java.lang.String,com.here.sdk.routing.TravelDirection,double,double,long)"
    class="section detail">

    ### SegmentReference

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SegmentReference</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> segmentId,
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

  - <div id="sdk-for-android-explore-<init>(java.lang.String,com.here.sdk.routing.TravelDirection,double,double,long,java.lang.Long)"
    class="section detail">

    ### SegmentReference

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SegmentReference</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> segmentId,
    @NonNull
    [TravelDirection](sdk-for-android-explore-com-here-sdk-routing-traveldirection "enum class in com.here.sdk.routing") travelDirection,
    double offsetStart, double offsetEnd, long tilePartitionId,
    @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" class="external-link" title="class or interface in java.lang">Long</a> localId)</span>

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

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-equals(java.lang.Object)"
    class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in
    class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode()" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in
    class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-fromString(java.lang.String)"
    class="section detail">

    ### fromString

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public
    static</span> <span class="return-type">[SegmentReference](sdk-for-android-explore-com-here-sdk-routing-segmentreference "class in com.here.sdk.routing")</span> <span class="element-name">fromString</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> segmentRef)</span>

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

