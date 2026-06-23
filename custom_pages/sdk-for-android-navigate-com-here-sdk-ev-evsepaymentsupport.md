---
title: "EVSEPaymentSupport (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-ev-evsepaymentsupport"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- EVSEPaymentSupport.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a>&gt;
<div class="inheritance">com.here.sdk.ev.EVSEPaymentSupport</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public enum </span><span class="element-name type-name-label">EVSEPaymentSupport</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a>&gt;</span></div>
<div class="block"><p>Represents the payment support functionality on EVSE for ad-hoc customers (without pre-registration).
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="inherited-list">

<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">Enum.EnumDesc</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a> extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a>&gt;&gt;</code></div>
</section>
</li>
<!-- =========== ENUM CONSTANT SUMMARY =========== -->
<li>
<section class="constants-summary" id="enum-constant-summary">

<div class="caption"><span>Enum Constants</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Enum Constant</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#AUTH_BY_CAR_AUTOCHARGE">AUTH_BY_CAR_AUTOCHARGE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Autocharge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#AUTH_BY_CAR_PLUG_AND_CHARGE">AUTH_BY_CAR_PLUG_AND_CHARGE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">ISO 15118 Plug&amp;Charge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#CHIP_CARD">CHIP_CARD</a></code></div>
<div class="col-last even-row-color">
<div class="block">EVSE has a payment terminal that supports chip cards.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#CONTACTLESS_CARD">CONTACTLESS_CARD</a></code></div>
<div class="col-last odd-row-color">
<div class="block">EVSE has a payment terminal that supports contactless cards.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#CREDIT_CARD">CREDIT_CARD</a></code></div>
<div class="col-last even-row-color">
<div class="block">EVSE has a payment terminal that makes it possible to pay for charging using a credit card.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#DEBIT_CARD">DEBIT_CARD</a></code></div>
<div class="col-last odd-row-color">
<div class="block">EVSE has a payment terminal that makes it possible to pay for charging using a debit card.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#MOBILE_PAYMENT">MOBILE_PAYMENT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Used with <a href="sdk-for-android-navigate-index#OPERATOR_APP"><code>OPERATOR_APP</code></a>,
 <a href="sdk-for-android-navigate-index#ONLINE_APPLE_PAY"><code>ONLINE_APPLE_PAY</code></a>,
 <a href="sdk-for-android-navigate-index#ONLINE_PAYPAL"><code>ONLINE_PAYPAL</code></a>,
 <a href="sdk-for-android-navigate-index#ONLINE_CREDIT_CARD"><code>ONLINE_CREDIT_CARD</code></a>,
 <a href="sdk-for-android-navigate-index#ONLINE_GOOGLE_PAY"><code>ONLINE_GOOGLE_PAY</code></a>,
 <a href="sdk-for-android-navigate-index#ONLINE_BANK_PAYMENT"><code>ONLINE_BANK_PAYMENT</code></a>,
 <a href="sdk-for-android-navigate-index#TERMINAL_SMS"><code>TERMINAL_SMS</code></a>,
 <a href="sdk-for-android-navigate-index#TERMINAL_QR_CODE"><code>TERMINAL_QR_CODE</code></a>, and
 <a href="sdk-for-android-navigate-index#CONTACTLESS_CARD"><code>CONTACTLESS_CARD</code></a>.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#ONLINE_APPLE_PAY">ONLINE_APPLE_PAY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Authenticate &amp; pay with Apple Pay.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#ONLINE_BANK_PAYMENT">ONLINE_BANK_PAYMENT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Authenticate &amp; pay with online bank payment.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#ONLINE_CREDIT_CARD">ONLINE_CREDIT_CARD</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Authenticate &amp; pay with credit card online.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#ONLINE_GOOGLE_PAY">ONLINE_GOOGLE_PAY</a></code></div>
<div class="col-last even-row-color">
<div class="block">Authenticate &amp; pay with Google Pay.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#ONLINE_PAYPAL">ONLINE_PAYPAL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Authenticate &amp; pay with PayPal.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#OPERATOR_APP">OPERATOR_APP</a></code></div>
<div class="col-last even-row-color">
<div class="block">Authenticate &amp; pay with charge point operator application on mobile phone.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#PED_TERMINAL">PED_TERMINAL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">EVSE has a payment terminal with a pin-code entry device.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RFID_READER">RFID_READER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Charging at this EVSE can be authorized with an RFID token.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#TERMINAL_QR_CODE">TERMINAL_QR_CODE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Initiate authentication &amp; payment with QR code on the terminal.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#TERMINAL_SMS">TERMINAL_SMS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Authenticate &amp; pay with SMS on the terminal.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#values()">values</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ ENUM CONSTANT DETAIL =========== -->
<li>
<section class="constant-details" id="enum-constant-detail">

<ul class="member-list">
<li>
<section class="detail" id="CHIP_CARD">
<h3>CHIP_CARD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">CHIP_CARD</span></div>
<div class="block"><p>EVSE has a payment terminal that supports chip cards.</p></div>
</section>
</li>
<li>
<section class="detail" id="CONTACTLESS_CARD">
<h3>CONTACTLESS_CARD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">CONTACTLESS_CARD</span></div>
<div class="block"><p>EVSE has a payment terminal that supports contactless cards.</p></div>
</section>
</li>
<li>
<section class="detail" id="CREDIT_CARD">
<h3>CREDIT_CARD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">CREDIT_CARD</span></div>
<div class="block"><p>EVSE has a payment terminal that makes it possible to pay for charging using a credit card.</p></div>
</section>
</li>
<li>
<section class="detail" id="DEBIT_CARD">
<h3>DEBIT_CARD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">DEBIT_CARD</span></div>
<div class="block"><p>EVSE has a payment terminal that makes it possible to pay for charging using a debit card.</p></div>
</section>
</li>
<li>
<section class="detail" id="PED_TERMINAL">
<h3>PED_TERMINAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">PED_TERMINAL</span></div>
<div class="block"><p>EVSE has a payment terminal with a pin-code entry device.</p></div>
</section>
</li>
<li>
<section class="detail" id="RFID_READER">
<h3>RFID_READER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">RFID_READER</span></div>
<div class="block"><p>Charging at this EVSE can be authorized with an RFID token.</p></div>
</section>
</li>
<li>
<section class="detail" id="AUTH_BY_CAR_PLUG_AND_CHARGE">
<h3>AUTH_BY_CAR_PLUG_AND_CHARGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">AUTH_BY_CAR_PLUG_AND_CHARGE</span></div>
<div class="block"><p>ISO 15118 Plug&amp;Charge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.</p></div>
</section>
</li>
<li>
<section class="detail" id="AUTH_BY_CAR_AUTOCHARGE">
<h3>AUTH_BY_CAR_AUTOCHARGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">AUTH_BY_CAR_AUTOCHARGE</span></div>
<div class="block"><p>Autocharge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.</p></div>
</section>
</li>
<li>
<section class="detail" id="ONLINE_APPLE_PAY">
<h3>ONLINE_APPLE_PAY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">ONLINE_APPLE_PAY</span></div>
<div class="block"><p>Authenticate &amp; pay with Apple Pay.</p></div>
</section>
</li>
<li>
<section class="detail" id="ONLINE_PAYPAL">
<h3>ONLINE_PAYPAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">ONLINE_PAYPAL</span></div>
<div class="block"><p>Authenticate &amp; pay with PayPal.</p></div>
</section>
</li>
<li>
<section class="detail" id="ONLINE_CREDIT_CARD">
<h3>ONLINE_CREDIT_CARD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">ONLINE_CREDIT_CARD</span></div>
<div class="block"><p>Authenticate &amp; pay with credit card online.</p></div>
</section>
</li>
<li>
<section class="detail" id="ONLINE_GOOGLE_PAY">
<h3>ONLINE_GOOGLE_PAY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">ONLINE_GOOGLE_PAY</span></div>
<div class="block"><p>Authenticate &amp; pay with Google Pay.</p></div>
</section>
</li>
<li>
<section class="detail" id="ONLINE_BANK_PAYMENT">
<h3>ONLINE_BANK_PAYMENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">ONLINE_BANK_PAYMENT</span></div>
<div class="block"><p>Authenticate &amp; pay with online bank payment.</p></div>
</section>
</li>
<li>
<section class="detail" id="TERMINAL_QR_CODE">
<h3>TERMINAL_QR_CODE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">TERMINAL_QR_CODE</span></div>
<div class="block"><p>Initiate authentication &amp; payment with QR code on the terminal.</p></div>
</section>
</li>
<li>
<section class="detail" id="TERMINAL_SMS">
<h3>TERMINAL_SMS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">TERMINAL_SMS</span></div>
<div class="block"><p>Authenticate &amp; pay with SMS on the terminal.</p></div>
</section>
</li>
<li>
<section class="detail" id="OPERATOR_APP">
<h3>OPERATOR_APP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">OPERATOR_APP</span></div>
<div class="block"><p>Authenticate &amp; pay with charge point operator application on mobile phone.</p></div>
</section>
</li>
<li>
<section class="detail" id="MOBILE_PAYMENT">
<h3>MOBILE_PAYMENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">MOBILE_PAYMENT</span></div>
<div class="block"><p>Used with <a href="sdk-for-android-navigate-index#OPERATOR_APP"><code>OPERATOR_APP</code></a>,
 <a href="sdk-for-android-navigate-index#ONLINE_APPLE_PAY"><code>ONLINE_APPLE_PAY</code></a>,
 <a href="sdk-for-android-navigate-index#ONLINE_PAYPAL"><code>ONLINE_PAYPAL</code></a>,
 <a href="sdk-for-android-navigate-index#ONLINE_CREDIT_CARD"><code>ONLINE_CREDIT_CARD</code></a>,
 <a href="sdk-for-android-navigate-index#ONLINE_GOOGLE_PAY"><code>ONLINE_GOOGLE_PAY</code></a>,
 <a href="sdk-for-android-navigate-index#ONLINE_BANK_PAYMENT"><code>ONLINE_BANK_PAYMENT</code></a>,
 <a href="sdk-for-android-navigate-index#TERMINAL_SMS"><code>TERMINAL_SMS</code></a>,
 <a href="sdk-for-android-navigate-index#TERMINAL_QR_CODE"><code>TERMINAL_QR_CODE</code></a>, and
 <a href="sdk-for-android-navigate-index#CONTACTLESS_CARD"><code>CONTACTLESS_CARD</code></a>.
 Whenever one or more of those payment types is specified,
 <a href="sdk-for-android-navigate-index#MOBILE_PAYMENT"><code>MOBILE_PAYMENT</code></a> is also specified.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="values()">
<h3>values</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a>[]</span> <span class="element-name">values</span>()</div>
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="valueOf(java.lang.String)">
<h3>valueOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-evsepaymentsupport" title="enum class in com.here.sdk.ev">EVSEPaymentSupport</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
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
`
}</HTMLBlock>
