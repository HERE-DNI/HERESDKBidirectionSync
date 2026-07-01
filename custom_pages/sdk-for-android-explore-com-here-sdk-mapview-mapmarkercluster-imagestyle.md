---
title: "MapMarkerCluster.ImageStyle (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-imagestyle"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.mapview.MapMarkerCluster.ImageStyle

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[MapMarkerCluster](sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">MapMarkerCluster.ImageStyle</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

This class specifies the visual appearance of a cluster marker.

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
  href="sdk-for-android-explore-com-here-sdk-core-anchor2d"
  title="class in com.here.sdk.core"><code>Anchor2D</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-imagestyle#anchor"
  class="member-name-link"><code>anchor</code></a></td>
  <td><div class="block">
  The anchor point for the marker image which specifies the position
  offset relative to the cluster's position.
  </div></td>
  </tr>
  <tr>
  <td><code>final </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapimage"
  title="class in com.here.sdk.mapview"><code>MapImage</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-imagestyle#image"
  class="member-name-link"><code>image</code></a></td>
  <td><div class="block">
  The map image for the cluster marker.
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
  <td><pre><code>ImageStyle(MapImage image)</code></pre></td>
  <td><div class="block">
  Creates a marker cluster image representation with default anchor.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>ImageStyle(MapImage image,
   Anchor2D anchor)</code></pre></td>
  <td><div class="block">
  Creates a cluster marker image style using a map image with anchor.
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

  - <div id="image" class="section detail">

    ### image

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    final</span> <span class="return-type">[MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview")</span> <span class="element-name">image</span>

    </div>

    <div class="block">

    The map image for the cluster marker.

    </div>

    </div>

  - <div id="anchor" class="section detail">

    ### anchor

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    final</span> <span class="return-type">[Anchor2D](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core")</span> <span class="element-name">anchor</span>

    </div>

    <div class="block">

    The anchor point for the marker image which specifies the position
    offset relative to the cluster's position.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.mapview.MapImage,com.here.sdk.core.Anchor2D)"
    class="section detail">

    ### ImageStyle

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ImageStyle</span><span class="parameters">(@NonNull
    [MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview") image,
    @NonNull
    [Anchor2D](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core") anchor)</span>

    </div>

    <div class="block">

    Creates a cluster marker image style using a map image with anchor.
    The anchor is a way of specifying position offset relative to
    image's dimensions on the screen. For example, (0, 0) places the
    top-left corner of the image at the cluster's position. (1, 1) would
    place the bottom-right corner of the image at the cluster's
    position.

    </div>

    Parameters:  
    `image` -

    The map image for the cluster marker.

    `anchor` -

    The anchor point for the marker image which specifies the position
    offset relative to the cluster's position.

    </div>

  - <div id="<init>(com.here.sdk.mapview.MapImage)"
    class="section detail">

    ### ImageStyle

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ImageStyle</span><span class="parameters">(@NonNull
    [MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview") image)</span>

    </div>

    <div class="block">

    Creates a marker cluster image representation with default anchor.

    </div>

    Parameters:  
    `image` -

    The map image for the cluster marker.

    </div>

  </div>

</div>

