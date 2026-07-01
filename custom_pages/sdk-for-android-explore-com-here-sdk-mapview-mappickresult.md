---
title: "MapPickResult (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mappickresult"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.mapview.MapPickResult
→ com.here.NativeBase → com.here.sdk.mapview.MapPickResult

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapPickResult</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

A class representing a map pick result.

</div>

</div>

<div class="section summary">

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
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapobjectdescriptor"
  title="class in com.here.sdk.mapview"><code>MapObjectDescriptor</code></a><code>&gt;</code></td>
  <td><pre><code>getCustomLayerObjectDescriptors()</code></pre></td>
  <td><div class="block">
  Gets a list of map object descriptors representing picked objects from
  custom user data layers.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-pickmapcontentresult"
  title="class in com.here.sdk.mapview"><code>PickMapContentResult</code></a></td>
  <td><pre><code>getMapContent()</code></pre></td>
  <td><div class="block">
  Gets a picked map content result.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-pickmapitemsresult"
  title="class in com.here.sdk.mapview"><code>PickMapItemsResult</code></a></td>
  <td><pre><code>getMapItems()</code></pre></td>
  <td><div class="block">
  Gets a picked map items result.
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

- <div id="method-detail" class="section method-details">

  - <div id="getMapItems()" class="section detail">

    ### getMapItems

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[PickMapItemsResult](sdk-for-android-explore-com-here-sdk-mapview-pickmapitemsresult "class in com.here.sdk.mapview")</span> <span class="element-name">getMapItems</span>()

    </div>

    <div class="block">

    Gets a picked map items result.

    </div>

    Returns:  
    Picked map items result.

    </div>

  - <div id="getMapContent()" class="section detail">

    ### getMapContent

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[PickMapContentResult](sdk-for-android-explore-com-here-sdk-mapview-pickmapcontentresult "class in com.here.sdk.mapview")</span> <span class="element-name">getMapContent</span>()

    </div>

    <div class="block">

    Gets a picked map content result.

    </div>

    Returns:  
    Picked map content result.

    </div>

  - <div id="getCustomLayerObjectDescriptors()" class="section detail">

    ### getCustomLayerObjectDescriptors

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapObjectDescriptor](sdk-for-android-explore-com-here-sdk-mapview-mapobjectdescriptor "class in com.here.sdk.mapview")></span> <span class="element-name">getCustomLayerObjectDescriptors</span>()

    </div>

    <div class="block">

    Gets a list of map object descriptors representing picked objects
    from custom user data layers.

    </div>

    Returns:  
    List of map object descriptors representing picked objects from
    custom user data layers.

    </div>

  </div>

</div>

