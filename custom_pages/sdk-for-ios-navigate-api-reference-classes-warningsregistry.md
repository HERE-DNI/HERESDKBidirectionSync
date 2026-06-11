---
title: "sdk-for-ios-navigate-api-reference-classes-warningsregistry"
slug: "sdk-for-ios-navigate-api-reference-classes-warningsregistry"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/WarningsRegistry"></a>
<a title="WarningsRegistry Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-warnerengine">WarnerEngine</a>
<img alt="" id="carat" src="/carat.png"/>
        WarningsRegistry Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>WarningsRegistry</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">WarningsRegistry</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">WarningsRegistry</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">WarningsRegistry</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A class that store warning metadata for different warning types.
Aggregates individual collection for each warning category (safety cameras, truck restrictions, etc.).
Provided by <code><a href="sdk-for-ios-navigate-api-reference-classes-warnerengine">WarnerEngine</a></code> so callers can lookup detailed information about specific warnings.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16WarningsRegistryC22getSafetyCameraWarning7warningAA0efG0VSgAA0G0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getSafetyCameraWarning(warning:)"></a>
<a class="token" href="#/s:7heresdk16WarningsRegistryC22getSafetyCameraWarning7warningAA0efG0VSgAA0G0V_tF">getSafetyCameraWarning(warning:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a safety-camera warning corresponding to the given identifier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getSafetyCameraWarning</span><span class="p">(</span><span class="nv">warning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warning">Warning</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-safetycamerawarning">SafetyCameraWarning</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warning</em>
</code>
</td>
<td>
<div>
<p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single safety-camera warning within this registry
and is used to retrieve its full metadata.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-safetycamerawarning">SafetyCameraWarning</a></code> object associated with the provided <code>WarningsRegistry.getSafetyCameraWarning(...).warning</code>,
or <code>nil</code> if no warning exists for the given <code>WarningsRegistry.getSafetyCameraWarning(...).warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16WarningsRegistryC26getTruckRestrictionWarning7warningAA0efG0VSgAA0G0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getTruckRestrictionWarning(warning:)"></a>
<a class="token" href="#/s:7heresdk16WarningsRegistryC26getTruckRestrictionWarning7warningAA0efG0VSgAA0G0V_tF">getTruckRestrictionWarning(warning:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a truck restrictions warning corresponding to the given identifier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getTruckRestrictionWarning</span><span class="p">(</span><span class="nv">warning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warning">Warning</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-truckrestrictionwarning">TruckRestrictionWarning</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warning</em>
</code>
</td>
<td>
<div>
<p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single truck restrictions warning within this registry
and is used to retrieve its full metadata.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-truckrestrictionwarning">TruckRestrictionWarning</a></code> object associated with the provided <code>WarningsRegistry.getTruckRestrictionWarning(...).warning</code>,
or <code>nil</code> if no warning exists for the given <code>WarningsRegistry.getTruckRestrictionWarning(...).warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16WarningsRegistryC18getRoadSignWarning7warningAA0efG0VSgAA0G0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getRoadSignWarning(warning:)"></a>
<a class="token" href="#/s:7heresdk16WarningsRegistryC18getRoadSignWarning7warningAA0efG0VSgAA0G0V_tF">getRoadSignWarning(warning:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a road-sign warning corresponding to the given identifier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getRoadSignWarning</span><span class="p">(</span><span class="nv">warning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warning">Warning</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-roadsignwarning">RoadSignWarning</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warning</em>
</code>
</td>
<td>
<div>
<p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single road sign warning within this registry
and is used to retrieve its full metadata.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>sdk.navigation.RoadSignWarning</code> object associated with the provided <code>WarningsRegistry.getRoadSignWarning(...).warning</code>,
or <code>nil</code> if no warning exists for the given <code>WarningsRegistry.getRoadSignWarning(...).warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16WarningsRegistryC23getRealisticViewWarning7warningAA0efG0VSgAA0G0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getRealisticViewWarning(warning:)"></a>
<a class="token" href="#/s:7heresdk16WarningsRegistryC23getRealisticViewWarning7warningAA0efG0VSgAA0G0V_tF">getRealisticViewWarning(warning:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a realistic-view warning corresponding to the given identifier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getRealisticViewWarning</span><span class="p">(</span><span class="nv">warning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warning">Warning</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-realisticviewwarning">RealisticViewWarning</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warning</em>
</code>
</td>
<td>
<div>
<p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single realistic-view warning within this registry
and is used to retrieve its full metadata.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-realisticviewwarning">RealisticViewWarning</a></code> object associated with the provided <code>WarningsRegistry.getRealisticViewWarning(...).warning</code>,
or <code>nil</code> if no warning exists for the given <code>WarningsRegistry.getRealisticViewWarning(...).warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16WarningsRegistryC27getEnvironmentalZoneWarning7warningAA0efG0VSgAA0G0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getEnvironmentalZoneWarning(warning:)"></a>
<a class="token" href="#/s:7heresdk16WarningsRegistryC27getEnvironmentalZoneWarning7warningAA0efG0VSgAA0G0V_tF">getEnvironmentalZoneWarning(warning:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns environmental zone warning corresponding to the given identifier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getEnvironmentalZoneWarning</span><span class="p">(</span><span class="nv">warning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warning">Warning</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-environmentalzonewarning">EnvironmentalZoneWarning</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warning</em>
</code>
</td>
<td>
<div>
<p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single environmental zone warning within this registry
and is used to retrieve its full metadata.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-environmentalzonewarning">EnvironmentalZoneWarning</a></code> object associated with the provided <code>WarningsRegistry.getEnvironmentalZoneWarning(...).warning</code>,
or <code>nil</code> if no warning exists for the given <code>WarningsRegistry.getEnvironmentalZoneWarning(...).warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16WarningsRegistryC20getSchoolZoneWarning7warningAA0efG0VSgAA0G0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getSchoolZoneWarning(warning:)"></a>
<a class="token" href="#/s:7heresdk16WarningsRegistryC20getSchoolZoneWarning7warningAA0efG0VSgAA0G0V_tF">getSchoolZoneWarning(warning:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a school zone warning corresponding to the given identifier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getSchoolZoneWarning</span><span class="p">(</span><span class="nv">warning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warning">Warning</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-schoolzonewarning">SchoolZoneWarning</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warning</em>
</code>
</td>
<td>
<div>
<p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single school zone warning within this registry
and is used to retrieve its full metadata.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-schoolzonewarning">SchoolZoneWarning</a></code> object associated with the provided <code>WarningsRegistry.getSchoolZoneWarning(...).warning</code>,
or <code>nil</code> if no warning exists for the given <code>WarningsRegistry.getSchoolZoneWarning(...).warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16WarningsRegistryC18getTollStopWarning7warningAA0eF0VSgAA0G0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getTollStopWarning(warning:)"></a>
<a class="token" href="#/s:7heresdk16WarningsRegistryC18getTollStopWarning7warningAA0eF0VSgAA0G0V_tF">getTollStopWarning(warning:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a toll stop warning corresponding to the given identifier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getTollStopWarning</span><span class="p">(</span><span class="nv">warning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warning">Warning</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-tollstop">TollStop</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warning</em>
</code>
</td>
<td>
<div>
<p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single toll stop warning within this registry
and is used to retrieve its full metadata.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-tollstop">TollStop</a></code> object associated with the provided <code>WarningsRegistry.getTollStopWarning(...).warning</code>,
or <code>nil</code> if no warning exists for the given <code>WarningsRegistry.getTollStopWarning(...).warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16WarningsRegistryC20getDangerZoneWarning7warningAA0efG0VSgAA0G0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getDangerZoneWarning(warning:)"></a>
<a class="token" href="#/s:7heresdk16WarningsRegistryC20getDangerZoneWarning7warningAA0efG0VSgAA0G0V_tF">getDangerZoneWarning(warning:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a danger zone warning corresponding to the given identifier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getDangerZoneWarning</span><span class="p">(</span><span class="nv">warning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warning">Warning</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-dangerzonewarning">DangerZoneWarning</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warning</em>
</code>
</td>
<td>
<div>
<p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single danger zone warning within this registry
and is used to retrieve its full metadata.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-dangerzonewarning">DangerZoneWarning</a></code> object associated with the provided <code>WarningsRegistry.getDangerZoneWarning(...).warning</code>,
or <code>nil</code> if no warning exists for the given <code>WarningsRegistry.getDangerZoneWarning(...).warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16WarningsRegistryC24getBorderCrossingWarning7warningAA0efG0VSgAA0G0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getBorderCrossingWarning(warning:)"></a>
<a class="token" href="#/s:7heresdk16WarningsRegistryC24getBorderCrossingWarning7warningAA0efG0VSgAA0G0V_tF">getBorderCrossingWarning(warning:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a border crossing warning corresponding to the given identifier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getBorderCrossingWarning</span><span class="p">(</span><span class="nv">warning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warning">Warning</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-bordercrossingwarning">BorderCrossingWarning</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warning</em>
</code>
</td>
<td>
<div>
<p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single border crossing warning within this registry
and is used to retrieve its full metadata.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-bordercrossingwarning">BorderCrossingWarning</a></code> object associated with the provided <code>WarningsRegistry.getBorderCrossingWarning(...).warning</code>,
or <code>nil</code> if no warning exists for the given <code>WarningsRegistry.getBorderCrossingWarning(...).warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16WarningsRegistryC25getRailwayCrossingWarning7warningAA0efG0VSgAA0G0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getRailwayCrossingWarning(warning:)"></a>
<a class="token" href="#/s:7heresdk16WarningsRegistryC25getRailwayCrossingWarning7warningAA0efG0VSgAA0G0V_tF">getRailwayCrossingWarning(warning:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a railway crossing warning corresponding to the given identifier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getRailwayCrossingWarning</span><span class="p">(</span><span class="nv">warning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warning">Warning</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-railwaycrossingwarning">RailwayCrossingWarning</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warning</em>
</code>
</td>
<td>
<div>
<p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single railway crossing warning within this registry
and is used to retrieve its full metadata.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-railwaycrossingwarning">RailwayCrossingWarning</a></code> object associated with the provided <code>WarningsRegistry.getRailwayCrossingWarning(...).warning</code>,
or <code>nil</code> if no warning exists for the given <code>WarningsRegistry.getRailwayCrossingWarning(...).warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16WarningsRegistryC22getLowSpeedZoneWarning7warningAA0efgH0VSgAA0H0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getLowSpeedZoneWarning(warning:)"></a>
<a class="token" href="#/s:7heresdk16WarningsRegistryC22getLowSpeedZoneWarning7warningAA0efgH0VSgAA0H0V_tF">getLowSpeedZoneWarning(warning:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a low speed zone warning corresponding to the given identifier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getLowSpeedZoneWarning</span><span class="p">(</span><span class="nv">warning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warning">Warning</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-lowspeedzonewarning">LowSpeedZoneWarning</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warning</em>
</code>
</td>
<td>
<div>
<p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single low speed zone warning within this registry
and is used to retrieve its full metadata.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-lowspeedzonewarning">LowSpeedZoneWarning</a></code> object associated with the provided <code>WarningsRegistry.getLowSpeedZoneWarning(...).warning</code>,
or <code>nil</code> if no warning exists for the given <code>WarningsRegistry.getLowSpeedZoneWarning(...).warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16WarningsRegistryC22getTrafficMergeWarning7warningAA0efG0VSgAA0G0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getTrafficMergeWarning(warning:)"></a>
<a class="token" href="#/s:7heresdk16WarningsRegistryC22getTrafficMergeWarning7warningAA0efG0VSgAA0G0V_tF">getTrafficMergeWarning(warning:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a traffic merge warning corresponding to the given identifier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getTrafficMergeWarning</span><span class="p">(</span><span class="nv">warning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warning">Warning</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-trafficmergewarning">TrafficMergeWarning</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warning</em>
</code>
</td>
<td>
<div>
<p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single traffic merge warning within this registry
and is used to retrieve its full metadata.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>sdk.navigation.TrafficMergeWarning</code> object associated with the provided <code>WarningsRegistry.getTrafficMergeWarning(...).warning</code>,
or <code>nil</code> if no warning exists for the given <code>WarningsRegistry.getTrafficMergeWarning(...).warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16WarningsRegistryC22getLaneDecreaseWarning7warningAA0efG0VSgAA0G0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getLaneDecreaseWarning(warning:)"></a>
<a class="token" href="#/s:7heresdk16WarningsRegistryC22getLaneDecreaseWarning7warningAA0efG0VSgAA0G0V_tF">getLaneDecreaseWarning(warning:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a lane decrease warning corresponding to the given identifier.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getLaneDecreaseWarning</span><span class="p">(</span><span class="nv">warning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warning">Warning</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-lanedecreasewarning">LaneDecreaseWarning</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warning</em>
</code>
</td>
<td>
<div>
<p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single lane decrease warning within this registry
and is used to retrieve its full metadata.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-lanedecreasewarning">LaneDecreaseWarning</a></code> object associated with the provided <code>WarningsRegistry.getLaneDecreaseWarning(...).warning</code>,
or <code>nil</code> if no warning exists for the given <code>WarningsRegistry.getLaneDecreaseWarning(...).warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16WarningsRegistryC16getCustomWarning7warningAA0eF0VSgAA0F0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getCustomWarning(warning:)"></a>
<a class="token" href="#/s:7heresdk16WarningsRegistryC16getCustomWarning7warningAA0eF0VSgAA0F0V_tF">getCustomWarning(warning:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns additional data associated with the given custom warning.</p>
<p>The provided <code>WarningsRegistry.getCustomWarning(...).warning</code> identifies a specific custom warning instance by its
base warning information and custom warning type. This information is used
to resolve the corresponding entry in the warning registry and retrieve
any additional, type-specific data associated with the warning.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getCustomWarning</span><span class="p">(</span><span class="nv">warning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warning">Warning</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-customwarning">CustomWarning</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warning</em>
</code>
</td>
<td>
<div>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-warning">Warning</a></code> instance identifying the custom warning for which
additional data should be retrieved.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-customwarning">CustomWarning</a></code> associated with the given <code>WarningsRegistry.getCustomWarning(...).warning</code>, or <code>nil</code>
if no additional data exists for this warning.
The returned object contains the payload with type-specific
details and attributes of the corresponding warning.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
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
}</HTMLBlock>
