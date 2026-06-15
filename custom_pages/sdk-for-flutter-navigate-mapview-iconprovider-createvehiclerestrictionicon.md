---
title: "createVehicleRestrictionIcon method"
slug: "sdk-for-flutter-navigate-mapview-iconprovider-createvehiclerestrictionicon"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- createVehicleRestrictionIcon.html -->


<div>
<h1>createVehicleRestrictionIcon method</h1></div>

void
createVehicleRestrictionIcon(<ol class="parameter-list"> <li><a href="sdk-for-flutter-navigate-mapview-pickvehiclerestrictionsresult-class">PickVehicleRestrictionsResult</a> pickingResult, </li>
<li><a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme</a> mapScheme, </li>
<li><a href="sdk-for-flutter-navigate-mapview-iconproviderassettype">IconProviderAssetType</a> assetType, </li>
<li><a href="sdk-for-flutter-navigate-core-size2d-class">Size2D</a> sizeConstraintsInPixels, </li>
<li><a href="sdk-for-flutter-navigate-mapview-iconprovidercallback">IconProviderCallback</a> callback, </li>
</ol>)

      

    

<p>Creates an image representing a vehicle restriction as shown on the map, based on map content picking result.</p>
<p><code>pickingResult</code> The result of picking vehicle restrictions.</p>
<p><code>mapScheme</code> The map scheme for which the vehicle restriction icon should be created.</p>
<p><code>assetType</code> The asset type for which the vehicle restriction icon should be created.</p>
<p><code>sizeConstraintsInPixels</code> The maximum width and height of the icon in pixels.
  The values are capped to a maximum of 4096 pixels. The image will be created as large as
  possible within the width and height constraints while maintaining the aspect ratio.
  If either width or height is set to 0, it will be calculated automatically based on icon's
  aspect ratio.</p>
<p><code>callback</code> The callback which is used to return the created image along with a description of the icon based on the
  type of road and/or place it is used, or an error code.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void createVehicleRestrictionIcon(
    PickVehicleRestrictionsResult pickingResult,
    MapScheme mapScheme,
    IconProviderAssetType assetType,
    Size2D sizeConstraintsInPixels,
    IconProviderCallback callback) {
  _createVehicleRestrictionIconWithPickResult(
      pickingResult, mapScheme, assetType, sizeConstraintsInPixels, callback);
}</code></pre>

 



</div>
`
}</HTMLBlock>
