---
title: "createVehicleRestrictionIconWithIconProperties method"
slug: "sdk-for-flutter-navigate-mapview-iconprovider-createvehiclerestrictioniconwithiconproperties"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- createVehicleRestrictionIconWithIconProperties.html -->


<div>
<h1>createVehicleRestrictionIconWithIconProperties method</h1></div>

void
createVehicleRestrictionIconWithIconProperties(<ol class="parameter-list"> <li><a href="sdk-for-flutter-navigate-mapview-vehiclerestrictioniconproperties-class">VehicleRestrictionIconProperties</a> properties, </li>
<li><a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme</a> mapScheme, </li>
<li><a href="sdk-for-flutter-navigate-mapview-iconproviderassettype">IconProviderAssetType</a> assetType, </li>
<li><a href="sdk-for-flutter-navigate-core-size2d-class">Size2D</a> sizeConstraintsInPixels, </li>
<li><a href="sdk-for-flutter-navigate-mapview-iconprovidercallback">IconProviderCallback</a> callback, </li>
</ol>)

      

    

<p>Creates an image representing a vehicle restriction as shown on the map.</p>
<p>In case when <a href="sdk-for-flutter-navigate-transport-vehiclerestriction-class">VehicleRestriction</a> object specifies multiple types of restrictions, then the icon is generated
for the first one according to the following priority: <a href="sdk-for-flutter-navigate-transport-vehiclerestriction-restriction">VehicleRestriction.restriction</a>, <a href="sdk-for-flutter-navigate-transport-vehiclerestriction-axlecount">VehicleRestriction.axleCount</a>,
<a href="sdk-for-flutter-navigate-transport-vehiclerestriction-axlecountingroup">VehicleRestriction.axleCountInGroup</a>, <a href="sdk-for-flutter-navigate-transport-vehiclerestriction-hazmatrestriction">VehicleRestriction.hazmatRestriction</a>, <a href="sdk-for-flutter-navigate-transport-vehiclerestriction-trailercount">VehicleRestriction.trailerCount</a>.</p>
<p><code>properties</code> The properties of a restriction icon to be created.</p>
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
<pre class="language-dart"><code class="language-dart">void createVehicleRestrictionIconWithIconProperties(
    VehicleRestrictionIconProperties properties,
    MapScheme mapScheme,
    IconProviderAssetType assetType,
    Size2D sizeConstraintsInPixels,
    IconProviderCallback callback) {
  _createVehicleRestrictionIconWithIconProperties(
      properties, mapScheme, assetType, sizeConstraintsInPixels, callback);
}</code></pre>

 



</div>
`
}</HTMLBlock>
