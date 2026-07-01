---
title: "IconProvider (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-iconprovider"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.mapview.IconProvider

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public class
</span><span class="element-name type-name-label">IconProvider</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

This provider creates icons from a given set of parameters for map
content and constraints for icon dimensions for a particular map scheme.
The icon creation currently does not rely on map data. Therefore, it
works without online connection. Note: This feature is in BETA state and
thus there can be bugs and unexpected behavior. Related APIs may change
for new releases without a deprecation process.

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
  <td><code>static interface </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-iconprovider-iconcallback"
  class="type-name-link"
  title="interface in com.here.sdk.mapview"><code>IconProvider.IconCallback</code></a></td>
  <td><div class="block">
  Interface which is used as callback to pass back an image or error code
  after calling the createRoadShieldIcon() method.
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
  <td><pre><code>IconProvider(MapContext mapContext)</code></pre></td>
  <td><div class="block">
  Creates an IconProvider.
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
  <td><code>void</code></td>
  <td><pre><code>createRoadShieldIcon(RoadShieldIconProperties properties,
   MapScheme mapScheme,
   IconProviderAssetType assetType,
   long widthConstraintInPixels,
   long heightConstraintInPixels,
   IconProvider.IconCallback callback)</code></pre></td>
  <td><div class="block">
  Creates an image displaying a road shield according to the given
  parameters.
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

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.mapview.MapContext)"
    class="section detail">

    ### IconProvider

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">IconProvider</span><span class="parameters">([MapContext](sdk-for-android-explore-com-here-sdk-mapview-mapcontext "class in com.here.sdk.mapview") mapContext)</span>

    </div>

    <div class="block">

    Creates an IconProvider.

    </div>

    Parameters:  
    `mapContext` - The map context instance.

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="createRoadShieldIcon(com.here.sdk.mapview.RoadShieldIconProperties,com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.IconProviderAssetType,long,long,com.here.sdk.mapview.IconProvider.IconCallback)"
    class="section detail">

    ### createRoadShieldIcon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">createRoadShieldIcon</span><span class="parameters">(@NonNull
    [RoadShieldIconProperties](sdk-for-android-explore-com-here-sdk-mapview-roadshieldiconproperties "class in com.here.sdk.mapview") properties,
    @NonNull
    [MapScheme](sdk-for-android-explore-com-here-sdk-mapview-mapscheme "enum class in com.here.sdk.mapview") mapScheme,
    @NonNull
    [IconProviderAssetType](sdk-for-android-explore-com-here-sdk-mapview-iconproviderassettype "enum class in com.here.sdk.mapview") assetType,
    long widthConstraintInPixels, long heightConstraintInPixels,
    @NonNull
    [IconProvider.IconCallback](sdk-for-android-explore-com-here-sdk-mapview-iconprovider-iconcallback "interface in com.here.sdk.mapview") callback)</span>

    </div>

    <div class="block">

    Creates an image displaying a road shield according to the given
    parameters.

    </div>

    Parameters:  
    `properties` - The properties which determine the kind of road
    shield to be created.

    `mapScheme` - The map scheme for which the road shield should be
    created.

    `assetType` - The asset type for which the road shield should be
    created.

    `widthConstraintInPixels` - The maximum width of the road shield in
    pixels. The value is capped to a maximum of 4096 pixels. The image
    will be created as large as possible within the width and height
    constraints while maintaining the aspect ratio. If set to 0, the
    width will be calculated based on the heightConstraintInPixels to
    preserve the aspect ratio.

    `heightConstraintInPixels` - The maximum height of the road shield
    in pixels. The value is capped to a maximum of 4096 pixels. The
    image will be created as large as possible within the width and
    height constraints while maintaining the aspect ratio. If set to 0,
    the original image-asset's height will be used.

    `callback` - The callback which is used to return the created image
    or an error code. Note: This feature is in BETA state and thus there
    can be bugs and unexpected behavior. Related APIs may change for new
    releases without a deprecation process.

    </div>

  </div>

</div>

