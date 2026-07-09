---
title: "EVSEPaymentSupport (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- EVSEPaymentSupport.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.ev</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a>&gt;
<div className="inheritance">com.here.sdk.ev.EVSEPaymentSupport</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a>&gt;</code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public enum </span><span className="element-name type-name-label">EVSEPaymentSupport</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a>&gt;</span></div>
<div className="block"><p>Represents the payment support functionality on EVSE for ad-hoc customers (without pre-registration).
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="inherited-list">

<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">Enum.EnumDesc</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a> extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a>&gt;&gt;</code></div>
</section>
</li>
<!-- =========== ENUM CONSTANT SUMMARY =========== -->
<li>
<section className="constants-summary" id="enum-constant-summary">

<div className="caption"><span>Enum Constants</span></div>
<div className="summary-table two-column-summary">


<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#AUTH_BY_CAR_AUTOCHARGE">AUTH_BY_CAR_AUTOCHARGE</a></code></div>
<div className="col-last even-row-color">
<div className="block">Autocharge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#AUTH_BY_CAR_PLUG_AND_CHARGE">AUTH_BY_CAR_PLUG_AND_CHARGE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">ISO 15118 Plug&amp;Charge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#CHIP_CARD">CHIP_CARD</a></code></div>
<div className="col-last even-row-color">
<div className="block">EVSE has a payment terminal that supports chip cards.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#CONTACTLESS_CARD">CONTACTLESS_CARD</a></code></div>
<div className="col-last odd-row-color">
<div className="block">EVSE has a payment terminal that supports contactless cards.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#CREDIT_CARD">CREDIT_CARD</a></code></div>
<div className="col-last even-row-color">
<div className="block">EVSE has a payment terminal that makes it possible to pay for charging using a credit card.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#DEBIT_CARD">DEBIT_CARD</a></code></div>
<div className="col-last odd-row-color">
<div className="block">EVSE has a payment terminal that makes it possible to pay for charging using a debit card.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#MOBILE_PAYMENT">MOBILE_PAYMENT</a></code></div>
<div className="col-last even-row-color">
<div className="block">Used with <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#OPERATOR_APP"><code>OPERATOR_APP</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#ONLINE_APPLE_PAY"><code>ONLINE_APPLE_PAY</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#ONLINE_PAYPAL"><code>ONLINE_PAYPAL</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#ONLINE_CREDIT_CARD"><code>ONLINE_CREDIT_CARD</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#ONLINE_GOOGLE_PAY"><code>ONLINE_GOOGLE_PAY</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#ONLINE_BANK_PAYMENT"><code>ONLINE_BANK_PAYMENT</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#TERMINAL_SMS"><code>TERMINAL_SMS</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#TERMINAL_QR_CODE"><code>TERMINAL_QR_CODE</code></a>, and
 <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#CONTACTLESS_CARD"><code>CONTACTLESS_CARD</code></a>.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#ONLINE_APPLE_PAY">ONLINE_APPLE_PAY</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Authenticate &amp; pay with Apple Pay.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#ONLINE_BANK_PAYMENT">ONLINE_BANK_PAYMENT</a></code></div>
<div className="col-last even-row-color">
<div className="block">Authenticate &amp; pay with online bank payment.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#ONLINE_CREDIT_CARD">ONLINE_CREDIT_CARD</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Authenticate &amp; pay with credit card online.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#ONLINE_GOOGLE_PAY">ONLINE_GOOGLE_PAY</a></code></div>
<div className="col-last even-row-color">
<div className="block">Authenticate &amp; pay with Google Pay.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#ONLINE_PAYPAL">ONLINE_PAYPAL</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Authenticate &amp; pay with PayPal.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#OPERATOR_APP">OPERATOR_APP</a></code></div>
<div className="col-last even-row-color">
<div className="block">Authenticate &amp; pay with charge point operator application on mobile phone.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#PED_TERMINAL">PED_TERMINAL</a></code></div>
<div className="col-last odd-row-color">
<div className="block">EVSE has a payment terminal with a pin-code entry device.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#RFID_READER">RFID_READER</a></code></div>
<div className="col-last even-row-color">
<div className="block">Charging at this EVSE can be authorized with an RFID token.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#TERMINAL_QR_CODE">TERMINAL_QR_CODE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Initiate authentication &amp; payment with QR code on the terminal.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#TERMINAL_SMS">TERMINAL_SMS</a></code></div>
<div className="col-last even-row-color">
<div className="block">Authenticate &amp; pay with SMS on the terminal.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ ENUM CONSTANT DETAIL =========== -->
<li>
<section className="constant-details" id="enum-constant-detail">

<ul className="member-list">
<li>
<section className="detail" id="CHIP_CARD">
<h3>CHIP_CARD</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">CHIP_CARD</span></div>
<div className="block"><p>EVSE has a payment terminal that supports chip cards.</p></div>
</section>
</li>
<li>
<section className="detail" id="CONTACTLESS_CARD">
<h3>CONTACTLESS_CARD</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">CONTACTLESS_CARD</span></div>
<div className="block"><p>EVSE has a payment terminal that supports contactless cards.</p></div>
</section>
</li>
<li>
<section className="detail" id="CREDIT_CARD">
<h3>CREDIT_CARD</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">CREDIT_CARD</span></div>
<div className="block"><p>EVSE has a payment terminal that makes it possible to pay for charging using a credit card.</p></div>
</section>
</li>
<li>
<section className="detail" id="DEBIT_CARD">
<h3>DEBIT_CARD</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">DEBIT_CARD</span></div>
<div className="block"><p>EVSE has a payment terminal that makes it possible to pay for charging using a debit card.</p></div>
</section>
</li>
<li>
<section className="detail" id="PED_TERMINAL">
<h3>PED_TERMINAL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">PED_TERMINAL</span></div>
<div className="block"><p>EVSE has a payment terminal with a pin-code entry device.</p></div>
</section>
</li>
<li>
<section className="detail" id="RFID_READER">
<h3>RFID_READER</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">RFID_READER</span></div>
<div className="block"><p>Charging at this EVSE can be authorized with an RFID token.</p></div>
</section>
</li>
<li>
<section className="detail" id="AUTH_BY_CAR_PLUG_AND_CHARGE">
<h3>AUTH_BY_CAR_PLUG_AND_CHARGE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">AUTH_BY_CAR_PLUG_AND_CHARGE</span></div>
<div className="block"><p>ISO 15118 Plug&amp;Charge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.</p></div>
</section>
</li>
<li>
<section className="detail" id="AUTH_BY_CAR_AUTOCHARGE">
<h3>AUTH_BY_CAR_AUTOCHARGE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">AUTH_BY_CAR_AUTOCHARGE</span></div>
<div className="block"><p>Autocharge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.</p></div>
</section>
</li>
<li>
<section className="detail" id="ONLINE_APPLE_PAY">
<h3>ONLINE_APPLE_PAY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">ONLINE_APPLE_PAY</span></div>
<div className="block"><p>Authenticate &amp; pay with Apple Pay.</p></div>
</section>
</li>
<li>
<section className="detail" id="ONLINE_PAYPAL">
<h3>ONLINE_PAYPAL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">ONLINE_PAYPAL</span></div>
<div className="block"><p>Authenticate &amp; pay with PayPal.</p></div>
</section>
</li>
<li>
<section className="detail" id="ONLINE_CREDIT_CARD">
<h3>ONLINE_CREDIT_CARD</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">ONLINE_CREDIT_CARD</span></div>
<div className="block"><p>Authenticate &amp; pay with credit card online.</p></div>
</section>
</li>
<li>
<section className="detail" id="ONLINE_GOOGLE_PAY">
<h3>ONLINE_GOOGLE_PAY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">ONLINE_GOOGLE_PAY</span></div>
<div className="block"><p>Authenticate &amp; pay with Google Pay.</p></div>
</section>
</li>
<li>
<section className="detail" id="ONLINE_BANK_PAYMENT">
<h3>ONLINE_BANK_PAYMENT</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">ONLINE_BANK_PAYMENT</span></div>
<div className="block"><p>Authenticate &amp; pay with online bank payment.</p></div>
</section>
</li>
<li>
<section className="detail" id="TERMINAL_QR_CODE">
<h3>TERMINAL_QR_CODE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">TERMINAL_QR_CODE</span></div>
<div className="block"><p>Initiate authentication &amp; payment with QR code on the terminal.</p></div>
</section>
</li>
<li>
<section className="detail" id="TERMINAL_SMS">
<h3>TERMINAL_SMS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">TERMINAL_SMS</span></div>
<div className="block"><p>Authenticate &amp; pay with SMS on the terminal.</p></div>
</section>
</li>
<li>
<section className="detail" id="OPERATOR_APP">
<h3>OPERATOR_APP</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">OPERATOR_APP</span></div>
<div className="block"><p>Authenticate &amp; pay with charge point operator application on mobile phone.</p></div>
</section>
</li>
<li>
<section className="detail" id="MOBILE_PAYMENT">
<h3>MOBILE_PAYMENT</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">MOBILE_PAYMENT</span></div>
<div className="block"><p>Used with <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#OPERATOR_APP"><code>OPERATOR_APP</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#ONLINE_APPLE_PAY"><code>ONLINE_APPLE_PAY</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#ONLINE_PAYPAL"><code>ONLINE_PAYPAL</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#ONLINE_CREDIT_CARD"><code>ONLINE_CREDIT_CARD</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#ONLINE_GOOGLE_PAY"><code>ONLINE_GOOGLE_PAY</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#ONLINE_BANK_PAYMENT"><code>ONLINE_BANK_PAYMENT</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#TERMINAL_SMS"><code>TERMINAL_SMS</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#TERMINAL_QR_CODE"><code>TERMINAL_QR_CODE</code></a>, and
 <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#CONTACTLESS_CARD"><code>CONTACTLESS_CARD</code></a>.
 Whenever one or more of those payment types is specified,
 <a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport#MOBILE_PAYMENT"><code>MOBILE_PAYMENT</code></a> is also specified.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="values()">
<h3>values</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a>[]</span> <span className="element-name">values</span>()</div>
<div className="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="valueOf(java.lang.String)">
<h3>valueOf</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span className="element-name">valueOf</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>
