---
title: "FuelType"
slug: "sdk-for-ios-navigate-enums-fueltype"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/FuelType"></a>
<a title="FuelType Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-search">Search</a>

        FuelType Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>FuelType</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">FuelType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Defines possible fuel types provided by a fuel station.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO6dieselyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/diesel"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO6dieselyA2CmF">diesel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Diesel fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">diesel</span> <span class="o">=</span> <span class="mi">1</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO3lpgyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/lpg"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO3lpgyA2CmF">lpg</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Liquified petroleum gas fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">lpg</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO9bioDieselyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/bioDiesel"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO9bioDieselyA2CmF">bioDiesel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Bio-Diesel fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">bioDiesel</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO3cngyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/cng"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO3cngyA2CmF">cng</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Compressed natural gas fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">cng</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO19dieselWithAdditivesyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/dieselWithAdditives"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO19dieselWithAdditivesyA2CmF">dieselWithAdditives</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Diesel with additives fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">dieselWithAdditives</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO3e10yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/e10"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO3e10yA2CmF">e10</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>10% Ethanol and 90% Gasoline fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">e10</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO3e20yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/e20"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO3e20yA2CmF">e20</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>20% Ethanol and 80% Gasoline fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">e20</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO3e85yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/e85"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO3e85yA2CmF">e85</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>85% Ethanol and 15% Gasoline fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">e85</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO7ethanolyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/ethanol"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO7ethanolyA2CmF">ethanol</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Ethanol fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">ethanol</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO20ethanolWithAdditivesyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/ethanolWithAdditives"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO20ethanolWithAdditivesyA2CmF">ethanolWithAdditives</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Ethanol with additives fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">ethanolWithAdditives</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO8gasolineyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/gasoline"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO8gasolineyA2CmF">gasoline</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gasoline fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">gasoline</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO9gasohol91yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/gasohol91"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO9gasohol91yA2CmF">gasohol91</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gasohol 91 fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">gasohol91</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO9gasohol95yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/gasohol95"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO9gasohol95yA2CmF">gasohol95</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gasohol 95 fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">gasohol95</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO3hvoyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/hvo"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO3hvoyA2CmF">hvo</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Hydrotreated vegetable oil fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">hvo</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO8hydrogenyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/hydrogen"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO8hydrogenyA2CmF">hydrogen</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Hydrogen fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">hydrogen</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO3lngyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/lng"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO3lngyA2CmF">lng</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Liquefied natural gas fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">lng</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO8midgradeyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/midgrade"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO8midgradeyA2CmF">midgrade</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Midgrade fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">midgrade</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO7premiumyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/premium"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO7premiumyA2CmF">premium</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Premium fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">premium</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO20premiumWithAdditivesyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/premiumWithAdditives"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO20premiumWithAdditivesyA2CmF">premiumWithAdditives</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Premium with additives fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">premiumWithAdditives</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO7regularyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/regular"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO7regularyA2CmF">regular</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Regular fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">regular</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO20regularWithAdditivesyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/regularWithAdditives"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO20regularWithAdditivesyA2CmF">regularWithAdditives</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Regular with additives fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">regularWithAdditives</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO8octane87yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/octane87"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO8octane87yA2CmF">octane87</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Octane 87 fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">octane87</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO8octane89yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/octane89"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO8octane89yA2CmF">octane89</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Octane 89 fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">octane89</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO8octane90yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/octane90"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO8octane90yA2CmF">octane90</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Octane 90 fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">octane90</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO8octane91yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/octane91"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO8octane91yA2CmF">octane91</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Octane 91 fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">octane91</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO8octane92yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/octane92"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO8octane92yA2CmF">octane92</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Octane 92 fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">octane92</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO8octane93yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/octane93"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO8octane93yA2CmF">octane93</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Octane 93 fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">octane93</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO8octane95yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/octane95"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO8octane95yA2CmF">octane95</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Octane 95 fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">octane95</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO8octane98yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/octane98"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO8octane98yA2CmF">octane98</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Octane 98 fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">octane98</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8FuelTypeO9octane100yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/octane100"></a>
<a class="token" href="#/s:7heresdk8FuelTypeO9octane100yA2CmF">octane100</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Octane 100 fuel type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">octane100</span></code></pre>
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
