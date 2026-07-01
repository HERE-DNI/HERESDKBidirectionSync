---
title: "MaxSpeedOnSegment (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-maxspeedonsegment"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.MaxSpeedOnSegment

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MaxSpeedOnSegment</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

New base speed for a segment. Affects route calculation and the ETA.
Cannot increase base speed on segment. Note: This option can only be
used with the RoutingEngine . The OfflineRoutingEngine is not supported
and the option will be ignored. Note that the OfflineRoutingEngine is
only available for the Navigate license.

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
  <td><code>double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-maxspeedonsegment#baseSpeedInMetersPerSecond"
  class="member-name-link"><code>baseSpeedInMetersPerSecond</code></a></td>
  <td><div class="block">
  New maximum value in m/s of baseSpeed on segment.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-segmentreference"
  title="class in com.here.sdk.routing"><code>SegmentReference</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-maxspeedonsegment#segment"
  class="member-name-link"><code>segment</code></a></td>
  <td><div class="block">
  A segment for which the new base speed is specified.
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
  <td><pre><code>MaxSpeedOnSegment(SegmentReference segment,
   double baseSpeedInMetersPerSecond)</code></pre></td>
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

  - <div id="segment" class="section detail">

    ### segment

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[SegmentReference](sdk-for-android-explore-com-here-sdk-routing-segmentreference "class in com.here.sdk.routing")</span> <span class="element-name">segment</span>

    </div>

    <div class="block">

    A segment for which the new base speed is specified. Only the
    segmendId and travelDirection parameters are used, other parameters
    are ignored. Setting a segmendId is mandatory. Note: The
    SegmentReference is not directly accessible from the map via the
    HERE SDK. Although, after route calculation you can retrieve the
    related segments for each Span . The segment IDs are the same that
    are also used by, for example, the Routing REST API . These IDs are
    mostly stable and only change when the underlying map data changes
    due to a new road or similar changes in the real world.

    </div>

    </div>

  - <div id="baseSpeedInMetersPerSecond" class="section detail">

    ### baseSpeedInMetersPerSecond

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">baseSpeedInMetersPerSecond</span>

    </div>

    <div class="block">

    New maximum value in m/s of baseSpeed on segment. The provided value
    must be in the range \[1.0, 70.0\]. Cannot increase base speed on
    segment. If the value is greater than the default base speed, then
    such penalty will have no effect.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.routing.SegmentReference,double)"
    class="section detail">

    ### MaxSpeedOnSegment

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MaxSpeedOnSegment</span><span class="parameters">(@NonNull
    [SegmentReference](sdk-for-android-explore-com-here-sdk-routing-segmentreference "class in com.here.sdk.routing") segment,
    double baseSpeedInMetersPerSecond)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `segment` -

    A segment for which the new base speed is specified. Only the
    `segmendId` and `travelDirection` parameters are used, other
    parameters are ignored. Setting a `segmendId` is mandatory.
    **Note:** The `SegmentReference` is not directly accessible from the
    map via the HERE SDK. Although, after route calculation you can
    retrieve the related segments for each
    [`Span`](sdk-for-android-explore-com-here-sdk-routing-span "class in com.here.sdk.routing").
    The segment IDs are the same that are also used by, for example, the
    [Routing REST
    API](https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/use-cases/avoid-segments.html).
    These IDs are mostly stable and only change when the underlying map
    data changes due to a new road or similar changes in the real world.

    `baseSpeedInMetersPerSecond` -

    New maximum value in m/s of baseSpeed on segment. The provided value
    must be in the range \[1.0, 70.0\]. Cannot increase base speed on
    segment. If the value is greater than the default base speed, then
    such penalty will have no effect.

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

