---
title: "PaymentMethod Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-enums-paymentmethod"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- PaymentMethod.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/PaymentMethod"></a>
<a title="PaymentMethod Enumeration Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Routing.html">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        PaymentMethod Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum PaymentMethod : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
<p>Available payment methods.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PaymentMethodO7unknownyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/unknown"></a>
<a class="token" href="#/s:7heresdk13PaymentMethodO7unknownyA2CmF">unknown</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Payment with an unknown method.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case unknown</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PaymentMethodO4cashyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/cash"></a>
<a class="token" href="#/s:7heresdk13PaymentMethodO4cashyA2CmF">cash</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Payment with cash money.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case cash</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PaymentMethodO8bankCardyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/bankCard"></a>
<a class="token" href="#/s:7heresdk13PaymentMethodO8bankCardyA2CmF">bankCard</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Payment with a bank card.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case bankCard</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PaymentMethodO10creditCardyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/creditCard"></a>
<a class="token" href="#/s:7heresdk13PaymentMethodO10creditCardyA2CmF">creditCard</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Payment with a credit card.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case creditCard</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PaymentMethodO16passSubscriptionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/passSubscription"></a>
<a class="token" href="#/s:7heresdk13PaymentMethodO16passSubscriptionyA2CmF">passSubscription</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Payment with a pass subscription.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case passSubscription</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PaymentMethodO11transponderyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/transponder"></a>
<a class="token" href="#/s:7heresdk13PaymentMethodO11transponderyA2CmF">transponder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Payment with a transponder.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case transponder</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PaymentMethodO9videoTollyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/videoToll"></a>
<a class="token" href="#/s:7heresdk13PaymentMethodO9videoTollyA2CmF">videoToll</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Payment with a video toll, i.e. toll by license plate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case videoToll</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PaymentMethodO9cashExactyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/cashExact"></a>
<a class="token" href="#/s:7heresdk13PaymentMethodO9cashExactyA2CmF">cashExact</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Payment with exact cash money, i.e. toll booth accepts exact change only.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case cashExact</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PaymentMethodO10travelCardyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/travelCard"></a>
<a class="token" href="#/s:7heresdk13PaymentMethodO10travelCardyA2CmF">travelCard</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Payment with a travel card.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case travelCard</code></pre>
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
