---
title: "IconProvider"
slug: "sdk-for-ios-explore-api-reference-classes-iconprovider"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/IconProvider"></a>
<a title="IconProvider Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-maps">Maps</a>

        IconProvider Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>IconProvider</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">IconProvider</span></code></pre>
</div>
</div>
<p>This provider creates icons from a given set of parameters for map content and constraints for
icon dimensions for a particular map scheme. The icon creation currently does not rely on map
data. Therefore, it works without online connection.</p>
<div class="aside aside-note">
<p class="aside-title">Note</p>
    This feature is in BETA state and thus there can be bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.

</div>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12IconProviderCyAcA10MapContextCcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk12IconProviderCyAcA10MapContextCcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Initializes an icon provider instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">mapContext</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcontext">MapContext</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapContext</em>
</code>
</td>
<td>
<div>
<p>The map context instance which is obtained using [MapView.mapContext].</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12IconProviderC016createRoadShieldB010properties9mapScheme9assetType23widthConstraintInPixels06heightmnO08callbackyAA0efB10PropertiesV_AA03MapI0OAA0bc5AssetK0Os6UInt32VARySo7UIImageCSg_SSSgAA0bC5ErrorOSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/createRoadShieldIcon(properties:mapScheme:assetType:widthConstraintInPixels:heightConstraintInPixels:callback:)"></a>
<a class="token" href="#/s:7heresdk12IconProviderC016createRoadShieldB010properties9mapScheme9assetType23widthConstraintInPixels06heightmnO08callbackyAA0efB10PropertiesV_AA03MapI0OAA0bc5AssetK0Os6UInt32VARySo7UIImageCSg_SSSgAA0bC5ErrorOSgtctF">createRoadShieldIcon(properties:<wbr/>mapScheme:<wbr/>assetType:<wbr/>widthConstraintInPixels:<wbr/>heightConstraintInPixels:<wbr/>callback:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an image displaying a road shield according to the given parameters.</p>
<div class="aside aside-note">
<p class="aside-title">Note</p>
    This feature is in BETA state and thus there can be bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">createRoadShieldIcon</span><span class="p">(</span>
    <span class="nv">properties</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-roadshieldiconproperties">RoadShieldIconProperties</a></span><span class="p">,</span>
    <span class="nv">mapScheme</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-mapscheme">MapScheme</a></span><span class="p">,</span>
    <span class="nv">assetType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-iconproviderassettype">IconProviderAssetType</a></span><span class="p">,</span>
    <span class="nv">widthConstraintInPixels</span><span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span>
    <span class="nv">heightConstraintInPixels</span><span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span>
    <span class="nv">callback</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Maps.html#/s:7heresdk20IconProviderCallbacka">IconProviderCallback</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>properties</em>
</code>
</td>
<td>
<div>
<p>The properties which determine the kind of road shield to be created.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>mapScheme</em>
</code>
</td>
<td>
<div>
<p>The map scheme for which the road shield should be created.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>assetType</em>
</code>
</td>
<td>
<div>
<p>The asset type for which the road shield should be created.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>widthConstraintInPixels</em>
</code>
</td>
<td>
<div>
<p>The maximum width of the road shield in pixels.
The value is capped to a maximum of 4096 pixels. The image will be created as large as
possible within the width and height constraints while maintaining the aspect ratio.
If set to 0, the width will be calculated based on the heightConstraintInPixels to
preserve the aspect ratio.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>heightConstraintInPixels</em>
</code>
</td>
<td>
<div>
<p>The maximum height of the road shield in pixels.
The value is capped to a maximum of 4096 pixels. The image will be created as large as
possible within the width and height constraints while maintaining the aspect ratio.
If set to 0, the original image-asset’s height will be used.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>callback</em>
</code>
</td>
<td>
<div>
<p>The callback which is used to return the created image along with a description of the icon based on the
type of road and/or place it is used, or an error code.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

`
} </HTMLBlock>
