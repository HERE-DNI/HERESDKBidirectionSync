---
title: "EVSEPaymentSupport Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-enums-evsepaymentsupport"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EVSEPaymentSupport.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/EVSEPaymentSupport"></a>
<a title="EVSEPaymentSupport Enumeration Reference"></a>
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
<a href="../EV.html">EV</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EVSEPaymentSupport Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum EVSEPaymentSupport : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
<p>Represents the payment support functionality on EVSE for ad-hoc customers (without pre-registration).
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVSEPaymentSupportO8chipCardyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/chipCard"></a>
<a class="token" href="#/s:7heresdk18EVSEPaymentSupportO8chipCardyA2CmF">chipCard</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>EVSE has a payment terminal that supports chip cards.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case chipCard</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVSEPaymentSupportO15contactlessCardyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/contactlessCard"></a>
<a class="token" href="#/s:7heresdk18EVSEPaymentSupportO15contactlessCardyA2CmF">contactlessCard</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>EVSE has a payment terminal that supports contactless cards.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case contactlessCard</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVSEPaymentSupportO10creditCardyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/creditCard"></a>
<a class="token" href="#/s:7heresdk18EVSEPaymentSupportO10creditCardyA2CmF">creditCard</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>EVSE has a payment terminal that makes it possible to pay for charging using a credit card.</p>
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
<a name="/s:7heresdk18EVSEPaymentSupportO9debitCardyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/debitCard"></a>
<a class="token" href="#/s:7heresdk18EVSEPaymentSupportO9debitCardyA2CmF">debitCard</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>EVSE has a payment terminal that makes it possible to pay for charging using a debit card.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case debitCard</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVSEPaymentSupportO11pedTerminalyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/pedTerminal"></a>
<a class="token" href="#/s:7heresdk18EVSEPaymentSupportO11pedTerminalyA2CmF">pedTerminal</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>EVSE has a payment terminal with a pin-code entry device.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case pedTerminal</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVSEPaymentSupportO10rfidReaderyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rfidReader"></a>
<a class="token" href="#/s:7heresdk18EVSEPaymentSupportO10rfidReaderyA2CmF">rfidReader</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Charging at this EVSE can be authorized with an RFID token.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rfidReader</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVSEPaymentSupportO22authByCarPlugAndChargeyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/authByCarPlugAndCharge"></a>
<a class="token" href="#/s:7heresdk18EVSEPaymentSupportO22authByCarPlugAndChargeyA2CmF">authByCarPlugAndCharge</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>ISO 15118 Plug&amp;Charge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case authByCarPlugAndCharge</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVSEPaymentSupportO19authByCarAutochargeyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/authByCarAutocharge"></a>
<a class="token" href="#/s:7heresdk18EVSEPaymentSupportO19authByCarAutochargeyA2CmF">authByCarAutocharge</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Autocharge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case authByCarAutocharge</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVSEPaymentSupportO14onlineApplePayyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/onlineApplePay"></a>
<a class="token" href="#/s:7heresdk18EVSEPaymentSupportO14onlineApplePayyA2CmF">onlineApplePay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Authenticate &amp; pay with Apple Pay.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case onlineApplePay</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVSEPaymentSupportO12onlinePaypalyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/onlinePaypal"></a>
<a class="token" href="#/s:7heresdk18EVSEPaymentSupportO12onlinePaypalyA2CmF">onlinePaypal</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Authenticate &amp; pay with PayPal.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case onlinePaypal</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVSEPaymentSupportO16onlineCreditCardyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/onlineCreditCard"></a>
<a class="token" href="#/s:7heresdk18EVSEPaymentSupportO16onlineCreditCardyA2CmF">onlineCreditCard</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Authenticate &amp; pay with credit card online.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case onlineCreditCard</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVSEPaymentSupportO15onlineGooglePayyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/onlineGooglePay"></a>
<a class="token" href="#/s:7heresdk18EVSEPaymentSupportO15onlineGooglePayyA2CmF">onlineGooglePay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Authenticate &amp; pay with Google Pay.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case onlineGooglePay</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVSEPaymentSupportO17onlineBankPaymentyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/onlineBankPayment"></a>
<a class="token" href="#/s:7heresdk18EVSEPaymentSupportO17onlineBankPaymentyA2CmF">onlineBankPayment</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Authenticate &amp; pay with online bank payment.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case onlineBankPayment</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVSEPaymentSupportO14terminalQrCodeyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/terminalQrCode"></a>
<a class="token" href="#/s:7heresdk18EVSEPaymentSupportO14terminalQrCodeyA2CmF">terminalQrCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Initiate authentication &amp; payment with QR code on the terminal.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case terminalQrCode</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVSEPaymentSupportO11terminalSmsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/terminalSms"></a>
<a class="token" href="#/s:7heresdk18EVSEPaymentSupportO11terminalSmsyA2CmF">terminalSms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Authenticate &amp; pay with SMS on the terminal.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case terminalSms</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVSEPaymentSupportO11operatorAppyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/operatorApp"></a>
<a class="token" href="#/s:7heresdk18EVSEPaymentSupportO11operatorAppyA2CmF">operatorApp</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Authenticate &amp; pay with charge point operator application on mobile phone.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case operatorApp</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVSEPaymentSupportO13mobilePaymentyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/mobilePayment"></a>
<a class="token" href="#/s:7heresdk18EVSEPaymentSupportO13mobilePaymentyA2CmF">mobilePayment</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Used with <code><a href="../Enums/EVSEPaymentSupport.html#/s:7heresdk18EVSEPaymentSupportO11operatorAppyA2CmF">EVSEPaymentSupport.operatorApp</a></code>,
<code><a href="../Enums/EVSEPaymentSupport.html#/s:7heresdk18EVSEPaymentSupportO14onlineApplePayyA2CmF">EVSEPaymentSupport.onlineApplePay</a></code>,
<code><a href="../Enums/EVSEPaymentSupport.html#/s:7heresdk18EVSEPaymentSupportO12onlinePaypalyA2CmF">EVSEPaymentSupport.onlinePaypal</a></code>,
<code><a href="../Enums/EVSEPaymentSupport.html#/s:7heresdk18EVSEPaymentSupportO16onlineCreditCardyA2CmF">EVSEPaymentSupport.onlineCreditCard</a></code>,
<code><a href="../Enums/EVSEPaymentSupport.html#/s:7heresdk18EVSEPaymentSupportO15onlineGooglePayyA2CmF">EVSEPaymentSupport.onlineGooglePay</a></code>,
<code><a href="../Enums/EVSEPaymentSupport.html#/s:7heresdk18EVSEPaymentSupportO17onlineBankPaymentyA2CmF">EVSEPaymentSupport.onlineBankPayment</a></code>,
<code><a href="../Enums/EVSEPaymentSupport.html#/s:7heresdk18EVSEPaymentSupportO11terminalSmsyA2CmF">EVSEPaymentSupport.terminalSms</a></code>,
<code><a href="../Enums/EVSEPaymentSupport.html#/s:7heresdk18EVSEPaymentSupportO14terminalQrCodeyA2CmF">EVSEPaymentSupport.terminalQrCode</a></code>, and
<code><a href="../Enums/EVSEPaymentSupport.html#/s:7heresdk18EVSEPaymentSupportO15contactlessCardyA2CmF">EVSEPaymentSupport.contactlessCard</a></code>.
Whenever one or more of those payment types is specified,
<code>EVSEPaymentSupport.mobilePayment</code> is also specified.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case mobilePayment</code></pre>
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
