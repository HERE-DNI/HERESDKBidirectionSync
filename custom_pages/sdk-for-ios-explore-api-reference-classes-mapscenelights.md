---
title: "MapSceneLights Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-mapscenelights"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MapSceneLights.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/MapSceneLights"></a>
<a title="MapSceneLights Class Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        MapSceneLights Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class MapSceneLights</code></pre>
<pre><code>extension MapSceneLights: NativeBase</code></pre>
<pre><code>extension MapSceneLights: Hashable</code></pre>
</div>
</div>
<p>Manage the lights and their attributes in a scene.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapSceneLightsC33AttributeSettingCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/AttributeSettingCompletionHandler"></a>
<a class="token" href="#/s:7heresdk14MapSceneLightsC33AttributeSettingCompletionHandlera">AttributeSettingCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This callback function allows handling errors that occur during the setting of light attributes.</p>
<p>Note: The error code <code>NO_LIGHTS</code> may be returned when attempting to set light attributes in map schemes
that do not support lights, for instance <code>road.network</code> map scheme.</p>
<p>Please refer to the error code documentation for further details on error handling.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias AttributeSettingCompletionHandler = (_ setLightError: MapSceneLights.AttributeSettingError?) -&gt; Void</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>setLightError</em>
</code>
</td>
<td>
<div>
<p>The cause for the failure when setting the light attributes, or <code>nil</code> if no error occurred.</p>
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
<a name="/s:7heresdk14MapSceneLightsC8CategoryO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/Category"></a>
<a class="token" href="#/s:7heresdk14MapSceneLightsC8CategoryO">Category</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The scene uses three categories of lighting which are:
Main light, Back light and Rim light.
These lights are directional lights.</p>
<p>The properties of all lights have an impact on the shading of 3D objects, for instance, extruded buildings within the scene.
However, shadow casting is only affected by the direction of the main light.</p>
<p>Category primarily serves as an identifier type for managing the lights.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-mapscenelights-category">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum Category : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapSceneLightsC21AttributeSettingErrorO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/AttributeSettingError"></a>
<a class="token" href="#/s:7heresdk14MapSceneLightsC21AttributeSettingErrorO">AttributeSettingError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Error enum indicating reasons for failure when setting light attributes.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-mapscenelights-attributesettingerror">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum AttributeSettingError : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapSceneLightsC9DirectionV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Direction"></a>
<a class="token" href="#/s:7heresdk14MapSceneLightsC9DirectionV">Direction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The direction of lights as a pair of azimuth and altitude angles.
See <a href="https://en.wikipedia.org/wiki/Horizontal_coordinate_system">https://en.wikipedia.org/wiki/Horizontal_coordinate_system</a></p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-mapscenelights-direction">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct Direction : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapSceneLightsC8setColor8category5color10completionyAC8CategoryO_So7UIColorCyAC21AttributeSettingErrorOSgcSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setColor(category:color:completion:)"></a>
<a class="token" href="#/s:7heresdk14MapSceneLightsC8setColor8category5color10completionyAC8CategoryO_So7UIColorCyAC21AttributeSettingErrorOSgcSgtF">setColor(category:<wbr/>color:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Set a new color for the light based on its category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func setColor(category: MapSceneLights.Category, color: UIColor, completion: MapSceneLights.AttributeSettingCompletionHandler?)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>category</em>
</code>
</td>
<td>
<div>
<p>The category of light for which the color is set.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>color</em>
</code>
</td>
<td>
<div>
<p>The Color type includes red, green, blue, and alpha components.
The value of these components must be inside the range [0, 1].</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Optional callback that will receive the result of this operation.</p>
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
<a name="/s:7heresdk14MapSceneLightsC12setIntensity8category9intensity10completionyAC8CategoryO_SdyAC21AttributeSettingErrorOSgcSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setIntensity(category:intensity:completion:)"></a>
<a class="token" href="#/s:7heresdk14MapSceneLightsC12setIntensity8category9intensity10completionyAC8CategoryO_SdyAC21AttributeSettingErrorOSgcSgtF">setIntensity(category:<wbr/>intensity:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Set a new intensity for the light based on its category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func setIntensity(category: MapSceneLights.Category, intensity: Double, completion: MapSceneLights.AttributeSettingCompletionHandler?)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>category</em>
</code>
</td>
<td>
<div>
<p>The category of light for which the intensity is set.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>intensity</em>
</code>
</td>
<td>
<div>
<p>The light intensity value must be inside the range [0, 10].
The intensity value is clamped to this range.
If the value falls outside its supported range, it will be adjusted to stay within the range.
Note: When the intensity value is big,
3D objects might turn completely white because all the color channels could go over the limit of 1.0.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Optional callback that will receive the result of this operation.</p>
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
<a name="/s:7heresdk14MapSceneLightsC12setDirection8category9direction10completionyAC8CategoryO_AC0F0VyAC21AttributeSettingErrorOSgcSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setDirection(category:direction:completion:)"></a>
<a class="token" href="#/s:7heresdk14MapSceneLightsC12setDirection8category9direction10completionyAC8CategoryO_AC0F0VyAC21AttributeSettingErrorOSgcSgtF">setDirection(category:<wbr/>direction:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Set a new direction for the light based on its category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func setDirection(category: MapSceneLights.Category, direction: MapSceneLights.Direction, completion: MapSceneLights.AttributeSettingCompletionHandler?)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>category</em>
</code>
</td>
<td>
<div>
<p>The category of light for which the direction is set.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>direction</em>
</code>
</td>
<td>
<div>
<p>The Direction contains azimuth and altitude angles in degrees.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Optional callback that will receive the result of this operation.</p>
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
<a name="/s:7heresdk14MapSceneLightsC8getColor8categorySo7UIColorCSgAC8CategoryO_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getColor(category:)"></a>
<a class="token" href="#/s:7heresdk14MapSceneLightsC8getColor8categorySo7UIColorCSgAC8CategoryO_tF">getColor(category:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Retrieves the current color of the light based on its category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getColor(category: MapSceneLights.Category) -&gt; UIColor?</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>category</em>
</code>
</td>
<td>
<div>
<p>The category of light from which the color is retrieved.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The current color of the light, or <code>nil</code> if the light is missing from the loaded scene
or MapScene is not intitialized.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapSceneLightsC12getIntensity8categorySdSgAC8CategoryO_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getIntensity(category:)"></a>
<a class="token" href="#/s:7heresdk14MapSceneLightsC12getIntensity8categorySdSgAC8CategoryO_tF">getIntensity(category:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Retrieves the current intensity of the light based on its category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getIntensity(category: MapSceneLights.Category) -&gt; Double?</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>category</em>
</code>
</td>
<td>
<div>
<p>The category of light from which the intensity is retrieved.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The current intensity of the light, or <code>nil</code> if the light is missing from the loaded scene
or MapScene is not intitialized.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapSceneLightsC12getDirection8categoryAC0F0VSgAC8CategoryO_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getDirection(category:)"></a>
<a class="token" href="#/s:7heresdk14MapSceneLightsC12getDirection8categoryAC0F0VSgAC8CategoryO_tF">getDirection(category:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Retrieves the current direction of the light based on its category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getDirection(category: MapSceneLights.Category) -&gt; MapSceneLights.Direction?</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>category</em>
</code>
</td>
<td>
<div>
<p>The category of light from which the direction is retrieved.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The current direction of the light, or <code>nil</code> if the light is missing from the loaded scene
or MapScene is not intitialized.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapSceneLightsC5resetyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/reset()"></a>
<a class="token" href="#/s:7heresdk14MapSceneLightsC5resetyyF">reset()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Resets all attributes of each light to their default values based on the current map scene settings.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func reset()</code></pre>
</div>
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



</div>
`
}</HTMLBlock>
