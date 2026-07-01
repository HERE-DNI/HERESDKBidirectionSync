---
title: "RouteOffset (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-routeoffset"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.RouteOffset

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">RouteOffset</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents a specific location along the route. A RouteOffset is a
location on the route defined by the section index and the distance in
meters from the start of that section to the specified location on the
route. An offset in meters indicates the distance that needs to be
traveled to reach a specific location along the route, such as a railway
crossing. For the latter case, the location of a railway crossing can be
retrieved from RouteRailwayCrossing.coordinates .

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
  href="sdk-for-android-explore-com-here-sdk-routing-routeoffset#offsetInMeters"
  class="member-name-link"><code>offsetInMeters</code></a></td>
  <td><div class="block">
  Offset from the start of the indexed Section to the specified location
  along the route.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routeoffset#sectionIndex"
  class="member-name-link"><code>sectionIndex</code></a></td>
  <td><div class="block">
  Index of the corresponding route Section .
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
  <td><pre><code>RouteOffset(int sectionIndex,
   double offsetInMeters)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
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

  - <div id="sectionIndex" class="section detail">

    ### sectionIndex

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">sectionIndex</span>

    </div>

    <div class="block">

    Index of the corresponding route Section . The start of the section
    indicates the start of the offset.

    </div>

    </div>

  - <div id="offsetInMeters" class="section detail">

    ### offsetInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">offsetInMeters</span>

    </div>

    <div class="block">

    Offset from the start of the indexed Section to the specified
    location along the route. The maximum possible offset is limited by
    the length of the section and cannot exceed it.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(int,double)" class="section detail">

    ### RouteOffset

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RouteOffset</span><span class="parameters">(int sectionIndex,
    double offsetInMeters)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `sectionIndex` -

    Index of the corresponding route
    [`Section`](sdk-for-android-explore-com-here-sdk-routing-section "class in com.here.sdk.routing").
    The start of the section indicates the start of the offset.

    `offsetInMeters` -

    Offset from the start of the indexed
    [`Section`](sdk-for-android-explore-com-here-sdk-routing-section "class in com.here.sdk.routing")
    to the specified location along the route. The maximum possible
    offset is limited by the length of the section and cannot exceed it.

    </div>

  </div>

</div>

