---
title: "createRoadShieldIcon method"
slug: "sdk-for-flutter-navigate-mapview-iconprovider-createroadshieldicon"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- createRoadShieldIcon.html -->


<div>
<h1>createRoadShieldIcon method</h1></div>

void
createRoadShieldIcon(<ol class="parameter-list"> <li><a href="sdk-for-flutter-navigate-mapview-roadshieldiconproperties-class">RoadShieldIconProperties</a> properties, </li>
<li><a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme</a> mapScheme, </li>
<li><a href="sdk-for-flutter-navigate-mapview-iconproviderassettype">IconProviderAssetType</a> assetType, </li>
<li>int widthConstraintInPixels, </li>
<li>int heightConstraintInPixels, </li>
<li><a href="sdk-for-flutter-navigate-mapview-iconprovidercallback">IconProviderCallback</a> callback, </li>
</ol>)

      

    

<p>Creates an image displaying a road shield according to the given parameters.</p>
<p><code>properties</code> The properties which determine the kind of road shield to be created.</p>
<p><code>mapScheme</code> The map scheme for which the road shield should be created.</p>
<p><code>assetType</code> The asset type for which the road shield should be created.</p>
<p><code>widthConstraintInPixels</code> The maximum width of the road shield in pixels.
  The value is capped to a maximum of 4096 pixels. The image will be created as large as
  possible within the width and height constraints while maintaining the aspect ratio.
  If set to 0, the width will be calculated based on the heightConstraintInPixels to
  preserve the aspect ratio.</p>
<p><code>heightConstraintInPixels</code> The maximum height of the road shield in pixels.
  The value is capped to a maximum of 4096 pixels. The image will be created as large as
  possible within the width and height constraints while maintaining the aspect ratio.
  If set to 0, the original image-asset's height will be used.</p>
<p><code>callback</code> The callback which is used to return the created image along with a description of the icon based on the
  type of road and/or place it is used, or an error code.</p>
<p>Note: This feature is in BETA state and thus there can be bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void createRoadShieldIcon(
    RoadShieldIconProperties properties,
    MapScheme mapScheme,
    IconProviderAssetType assetType,
    int widthConstraintInPixels,
    int heightConstraintInPixels,
    IconProviderCallback callback) {
  _createRoadShieldIcon(properties, mapScheme, assetType,
      widthConstraintInPixels, heightConstraintInPixels, callback);
}</code></pre>

 



</div>
`
}</HTMLBlock>
