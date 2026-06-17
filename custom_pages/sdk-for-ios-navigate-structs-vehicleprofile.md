---
title: "VehicleProfile"
slug: "sdk-for-ios-navigate-structs-vehicleprofile"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/VehicleProfile"></a>
<a title="VehicleProfile Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-transport">Transport</a>

        VehicleProfile Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VehicleProfile</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use sdk.transport.TransportSpecification instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">VehicleProfile</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A vehicle profile describes the vehicle being used with the HSDK.</p>
<p>The profile is planned to be used as single source of information describing the vehicle.</p>
<p>Current modules that use this profile:</p>
<ul>
<li>Navigation: Tracking mode for truck related vehicle restrictions.</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this vehicle profile, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases or even become unsupported, without a
deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VehicleProfileV11vehicleTypeAA0bE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/vehicleType"></a>
<a class="token" href="#/s:7heresdk14VehicleProfileV11vehicleTypeAA0bE0Ovp">vehicleType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the vehicle type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">vehicleType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-vehicletype">VehicleType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VehicleProfileV13truckCategoryAA05TruckE0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckCategory"></a>
<a class="token" href="#/s:7heresdk14VehicleProfileV13truckCategoryAA05TruckE0OSgvp">truckCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the truck category.
Only used when the <code><a href="../Structs/VehicleProfile.html#/s:7heresdk14VehicleProfileV11vehicleTypeAA0bE0Ovp">VehicleProfile.vehicleType</a></code> is <code><a href="../Enums/VehicleType.html#/s:7heresdk11VehicleTypeO5truckyA2CmF">VehicleType.truck</a></code>
By default, it is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">truckCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-truckcategory">TruckCategory</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VehicleProfileV12trailerCounts5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trailerCount"></a>
<a class="token" href="#/s:7heresdk14VehicleProfileV12trailerCounts5Int32Vvp">trailerCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines number of trailers attached to the vehicle. The provided value must be in the range
[0, 255]. When not set, possible trailer count restrictions will not be taken into consideration
for route calculation. By default, it is 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trailerCount</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VehicleProfileV18hazardousMaterialsSayAA17HazardousMaterialOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/hazardousMaterials"></a>
<a class="token" href="#/s:7heresdk14VehicleProfileV18hazardousMaterialsSayAA17HazardousMaterialOGvp">hazardousMaterials</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies a list of hazardous materials shipped in the vehicle.
Refer to <code><a href="sdk-for-ios-navigate-enums-hazardousmaterial">HazardousMaterial</a></code> for the available options.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">hazardousMaterials</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-enums-hazardousmaterial">HazardousMaterial</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VehicleProfileV14tunnelCategoryAA06TunnelE0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tunnelCategory"></a>
<a class="token" href="#/s:7heresdk14VehicleProfileV14tunnelCategoryAA06TunnelE0OSgvp">tunnelCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the tunnel categories to restrict certain route links.
The route will pass only through tunnels of a less strict category.
Refer to <code><a href="sdk-for-ios-navigate-enums-tunnelcategory">TunnelCategory</a></code> for the available options.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tunnelCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-tunnelcategory">TunnelCategory</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VehicleProfileV9axleCounts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/axleCount"></a>
<a class="token" href="#/s:7heresdk14VehicleProfileV9axleCounts5Int32VSgvp">axleCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines total number of axles in the vehicle. The provided value must be greater than or
equal to 2. When not set, possible axle count restrictions will not be taken into
consideration for route calculation. By default, it is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">axleCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VehicleProfileV22grossWeightInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/grossWeightInKilograms"></a>
<a class="token" href="#/s:7heresdk14VehicleProfileV22grossWeightInKilogramss5Int32VSgvp">grossWeightInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle weight including trailers and shipped goods in kilograms.
By default, it is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">grossWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VehicleProfileV19heightInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/heightInCentimeters"></a>
<a class="token" href="#/s:7heresdk14VehicleProfileV19heightInCentimeterss5Int32VSgvp">heightInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle height in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">heightInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VehicleProfileV19lengthInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lengthInCentimeters"></a>
<a class="token" href="#/s:7heresdk14VehicleProfileV19lengthInCentimeterss5Int32VSgvp">lengthInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle length in centimeters. The provided value must be in the range [0, 30000].
By default, it is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lengthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VehicleProfileV18widthInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/widthInCentimeters"></a>
<a class="token" href="#/s:7heresdk14VehicleProfileV18widthInCentimeterss5Int32VSgvp">widthInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle width in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">widthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VehicleProfileV24weightPerAxleInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/weightPerAxleInKilograms"></a>
<a class="token" href="#/s:7heresdk14VehicleProfileV24weightPerAxleInKilogramss5Int32VSgvp">weightPerAxleInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle weight per axle in kilograms. The provided value must be greater or equal to 0.
When not set, possible weight per axle restrictions will not be taken into
consideration for route calculation. By default, it is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">weightPerAxleInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VehicleProfileV11vehicleType13truckCategory12trailerCount18hazardousMaterials06tunnelG004axleI022grossWeightInKilograms06heightP11Centimeters06lengthpS005widthpS0013weightPerAxlepQ0AcA0bE0O_AA05TruckG0OSgs5Int32VSayAA17HazardousMaterialOGAA06TunnelG0OSgAUSgA0_A0_A0_A0_A0_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(vehicleType:truckCategory:trailerCount:hazardousMaterials:tunnelCategory:axleCount:grossWeightInKilograms:heightInCentimeters:lengthInCentimeters:widthInCentimeters:weightPerAxleInKilograms:)"></a>
<a class="token" href="#/s:7heresdk14VehicleProfileV11vehicleType13truckCategory12trailerCount18hazardousMaterials06tunnelG004axleI022grossWeightInKilograms06heightP11Centimeters06lengthpS005widthpS0013weightPerAxlepQ0AcA0bE0O_AA05TruckG0OSgs5Int32VSayAA17HazardousMaterialOGAA06TunnelG0OSgAUSgA0_A0_A0_A0_A0_tcfc">init(vehicleType:<wbr/>truckCategory:<wbr/>trailerCount:<wbr/>hazardousMaterials:<wbr/>tunnelCategory:<wbr/>axleCount:<wbr/>grossWeightInKilograms:<wbr/>heightInCentimeters:<wbr/>lengthInCentimeters:<wbr/>widthInCentimeters:<wbr/>weightPerAxleInKilograms:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">vehicleType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-vehicletype">VehicleType</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-vehicletype">VehicleType</a></span><span class="o">.</span><span class="n">car</span><span class="p">,</span> <span class="nv">truckCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-truckcategory">TruckCategory</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">trailerCount</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">hazardousMaterials</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-enums-hazardousmaterial">HazardousMaterial</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">tunnelCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-tunnelcategory">TunnelCategory</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">axleCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">grossWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">heightInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">lengthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">widthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">weightPerAxleInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
</body>
</html>

`
} </HTMLBlock>
