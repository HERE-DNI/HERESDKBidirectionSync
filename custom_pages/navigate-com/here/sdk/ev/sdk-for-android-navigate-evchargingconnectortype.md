---
title: "EVChargingConnectorType (API Reference)"
slug: "sdk-for-android-navigate-evchargingconnectortype"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- EVChargingConnectorType.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li><a href="#field-summary">Field</a> | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li><a href="#field-detail">Field</a> | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
<li>Method</li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.ev</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.ev.EVChargingConnectorType</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">EVChargingConnectorType</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Represents the standardized type of the installed connector.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CHADEMO">CHADEMO</a></code></div>
<div class="col-last even-row-color">
<div class="block">The connector type is CHAdeMO, DC.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CHAOJI">CHAOJI</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The ChaoJi connector.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DOMESTIC_A">DOMESTIC_A</a></code></div>
<div class="col-last even-row-color">
<div class="block">Standard/Domestic household, type "A", NEMA 1-15, 2 pins.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DOMESTIC_B">DOMESTIC_B</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Standard/Domestic household, type "B", NEMA 5-15, 3 pins.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DOMESTIC_C">DOMESTIC_C</a></code></div>
<div class="col-last even-row-color">
<div class="block">Standard/Domestic household, type "C", CEE 7/17, 2 pins.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DOMESTIC_D">DOMESTIC_D</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Standard/Domestic household, type "D", 3 pin.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DOMESTIC_E">DOMESTIC_E</a></code></div>
<div class="col-last even-row-color">
<div class="block">Standard/Domestic household, type "E", CEE 7/5 3 pins.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DOMESTIC_F">DOMESTIC_F</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Standard/Domestic household, type "F", CEE 7/4, Schuko, 3 pins.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DOMESTIC_G">DOMESTIC_G</a></code></div>
<div class="col-last even-row-color">
<div class="block">Standard/Domestic household, type "G", BS 1363, Commonwealth, 3 pins.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DOMESTIC_H">DOMESTIC_H</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Standard/Domestic household, type "H", SI-32, 3 pins.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DOMESTIC_I">DOMESTIC_I</a></code></div>
<div class="col-last even-row-color">
<div class="block">Standard/Domestic household, type "I", AS 3112, 3 pins.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DOMESTIC_J">DOMESTIC_J</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Standard/Domestic household, type "J", SEV 1011, 3 pins.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DOMESTIC_K">DOMESTIC_K</a></code></div>
<div class="col-last even-row-color">
<div class="block">Standard/Domestic household, type "K", DS 60884-2-D1, 3 pins.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DOMESTIC_L">DOMESTIC_L</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Standard/Domestic household, type "L", CEI 23-16-VII, 3 pins.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DOMESTIC_M">DOMESTIC_M</a></code></div>
<div class="col-last even-row-color">
<div class="block">Standard/Domestic household, type "M", BS 546, 3 pins.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DOMESTIC_N">DOMESTIC_N</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Standard/Domestic household, type "N", NBR 14136, 3 pins.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DOMESTIC_O">DOMESTIC_O</a></code></div>
<div class="col-last even-row-color">
<div class="block">Standard/Domestic household, type "O", TIS 166-2549, 3 pins.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#GBT_AC">GBT_AC</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Guobiao GB/T 20234.2 AC socket/connector.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#GBT_DC">GBT_DC</a></code></div>
<div class="col-last even-row-color">
<div class="block">Guobiao GB/T 20234.3 DC connector.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#IEC_60309_2_SINGLE_16">IEC_60309_2_SINGLE_16</a></code></div>
<div class="col-last odd-row-color">
<div class="block">IEC 60309-2 Industrial connector single phase 16 amperes (usually blue).</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#IEC_60309_2_THREE_16">IEC_60309_2_THREE_16</a></code></div>
<div class="col-last even-row-color">
<div class="block">IEC 60309-2 Industrial connector three phase 16 amperes (usually red).</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#IEC_60309_2_THREE_32">IEC_60309_2_THREE_32</a></code></div>
<div class="col-last odd-row-color">
<div class="block">IEC 60309-2 Industrial connector three phase 32 amperes (usually red).</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#IEC_60309_2_THREE_64">IEC_60309_2_THREE_64</a></code></div>
<div class="col-last even-row-color">
<div class="block">IEC 60309-2 Industrial connector three phase 64 amperes (usually red).</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#IEC_62196_T1">IEC_62196_T1</a></code></div>
<div class="col-last odd-row-color">
<div class="block">IEC 62196 Type 1 "SAE J1772".</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#IEC_62196_T1_COMBO">IEC_62196_T1_COMBO</a></code></div>
<div class="col-last even-row-color">
<div class="block">Combo Type 1 based, DC.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#IEC_62196_T2">IEC_62196_T2</a></code></div>
<div class="col-last odd-row-color">
<div class="block">IEC 62196 Type 2 "Mennekes".</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#IEC_62196_T2_COMBO">IEC_62196_T2_COMBO</a></code></div>
<div class="col-last even-row-color">
<div class="block">Combo Type 2 based, DC.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#IEC_62196_T3A">IEC_62196_T3A</a></code></div>
<div class="col-last odd-row-color">
<div class="block">IEC 62196 Type 3A.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#IEC_62196_T3C">IEC_62196_T3C</a></code></div>
<div class="col-last even-row-color">
<div class="block">IEC 62196 Type 3C "Scame".</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MCS">MCS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Megawatt Charging System (MCS) connector.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NEMA_10_30">NEMA_10_30</a></code></div>
<div class="col-last even-row-color">
<div class="block">NEMA 10-30, 3 pins.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NEMA_10_50">NEMA_10_50</a></code></div>
<div class="col-last odd-row-color">
<div class="block">NEMA 10-50, 3 pins.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NEMA_14_30">NEMA_14_30</a></code></div>
<div class="col-last even-row-color">
<div class="block">NEMA 14-30, 4 pins.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NEMA_14_50">NEMA_14_50</a></code></div>
<div class="col-last odd-row-color">
<div class="block">NEMA 14-50, 4 pins.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NEMA_5_20">NEMA_5_20</a></code></div>
<div class="col-last even-row-color">
<div class="block">NEMA 5-20, 3 pins.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NEMA_6_30">NEMA_6_30</a></code></div>
<div class="col-last odd-row-color">
<div class="block">NEMA 6-30, 3 pins.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NEMA_6_50">NEMA_6_50</a></code></div>
<div class="col-last even-row-color">
<div class="block">NEMA 6-50, 3 pins.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PANTOGRAPH_BOTTOM_UP">PANTOGRAPH_BOTTOM_UP</a></code></div>
<div class="col-last odd-row-color">
<div class="block">On-board Bottom-up-Pantograph typically for bus charging.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PANTOGRAPH_TOP_DOWN">PANTOGRAPH_TOP_DOWN</a></code></div>
<div class="col-last even-row-color">
<div class="block">Top-down-Pantograph typically for bus charging.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SAE_J3400">SAE_J3400</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Tesla connector "Model-S"-type (oval, 5 pin), standardized as NACS SAE J3400.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TESLA_R">TESLA_R</a></code></div>
<div class="col-last even-row-color">
<div class="block">Tesla connector "Roadster"-type (round, 4 pin).</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">EVChargingConnectorType</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="CHADEMO">
<h3>CHADEMO</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CHADEMO</span></div>
<div class="block"><p>The connector type is CHAdeMO, DC.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.CHADEMO">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CHAOJI">
<h3>CHAOJI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CHAOJI</span></div>
<div class="block"><p>The ChaoJi connector. The new generation charging connector, harmonized between CHAdeMO and GB/T. DC.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.CHAOJI">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOMESTIC_A">
<h3>DOMESTIC_A</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_A</span></div>
<div class="block"><p>Standard/Domestic household, type "A", NEMA 1-15, 2 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_A">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOMESTIC_B">
<h3>DOMESTIC_B</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_B</span></div>
<div class="block"><p>Standard/Domestic household, type "B", NEMA 5-15, 3 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_B">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOMESTIC_C">
<h3>DOMESTIC_C</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_C</span></div>
<div class="block"><p>Standard/Domestic household, type "C", CEE 7/17, 2 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_C">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOMESTIC_D">
<h3>DOMESTIC_D</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_D</span></div>
<div class="block"><p>Standard/Domestic household, type "D", 3 pin.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_D">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOMESTIC_E">
<h3>DOMESTIC_E</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_E</span></div>
<div class="block"><p>Standard/Domestic household, type "E", CEE 7/5 3 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_E">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOMESTIC_F">
<h3>DOMESTIC_F</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_F</span></div>
<div class="block"><p>Standard/Domestic household, type "F", CEE 7/4, Schuko, 3 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_F">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOMESTIC_G">
<h3>DOMESTIC_G</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_G</span></div>
<div class="block"><p>Standard/Domestic household, type "G", BS 1363, Commonwealth, 3 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_G">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOMESTIC_H">
<h3>DOMESTIC_H</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_H</span></div>
<div class="block"><p>Standard/Domestic household, type "H", SI-32, 3 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_H">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOMESTIC_I">
<h3>DOMESTIC_I</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_I</span></div>
<div class="block"><p>Standard/Domestic household, type "I", AS 3112, 3 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_I">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOMESTIC_J">
<h3>DOMESTIC_J</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_J</span></div>
<div class="block"><p>Standard/Domestic household, type "J", SEV 1011, 3 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_J">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOMESTIC_K">
<h3>DOMESTIC_K</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_K</span></div>
<div class="block"><p>Standard/Domestic household, type "K", DS 60884-2-D1, 3 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_K">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOMESTIC_L">
<h3>DOMESTIC_L</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_L</span></div>
<div class="block"><p>Standard/Domestic household, type "L", CEI 23-16-VII, 3 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_L">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOMESTIC_M">
<h3>DOMESTIC_M</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_M</span></div>
<div class="block"><p>Standard/Domestic household, type "M", BS 546, 3 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_M">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOMESTIC_N">
<h3>DOMESTIC_N</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_N</span></div>
<div class="block"><p>Standard/Domestic household, type "N", NBR 14136, 3 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_N">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOMESTIC_O">
<h3>DOMESTIC_O</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_O</span></div>
<div class="block"><p>Standard/Domestic household, type "O", TIS 166-2549, 3 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_O">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="GBT_AC">
<h3>GBT_AC</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">GBT_AC</span></div>
<div class="block"><p>Guobiao GB/T 20234.2 AC socket/connector.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.GBT_AC">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="GBT_DC">
<h3>GBT_DC</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">GBT_DC</span></div>
<div class="block"><p>Guobiao GB/T 20234.3 DC connector.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.GBT_DC">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IEC_60309_2_SINGLE_16">
<h3>IEC_60309_2_SINGLE_16</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_60309_2_SINGLE_16</span></div>
<div class="block"><p>IEC 60309-2 Industrial connector single phase 16 amperes (usually blue).</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_60309_2_SINGLE_16">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IEC_60309_2_THREE_16">
<h3>IEC_60309_2_THREE_16</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_60309_2_THREE_16</span></div>
<div class="block"><p>IEC 60309-2 Industrial connector three phase 16 amperes (usually red).</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_60309_2_THREE_16">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IEC_60309_2_THREE_32">
<h3>IEC_60309_2_THREE_32</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_60309_2_THREE_32</span></div>
<div class="block"><p>IEC 60309-2 Industrial connector three phase 32 amperes (usually red).</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_60309_2_THREE_32">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IEC_60309_2_THREE_64">
<h3>IEC_60309_2_THREE_64</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_60309_2_THREE_64</span></div>
<div class="block"><p>IEC 60309-2 Industrial connector three phase 64 amperes (usually red).</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_60309_2_THREE_64">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IEC_62196_T1">
<h3>IEC_62196_T1</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_62196_T1</span></div>
<div class="block"><p>IEC 62196 Type 1 "SAE J1772".</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_62196_T1">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IEC_62196_T1_COMBO">
<h3>IEC_62196_T1_COMBO</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_62196_T1_COMBO</span></div>
<div class="block"><p>Combo Type 1 based, DC.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_62196_T1_COMBO">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IEC_62196_T2">
<h3>IEC_62196_T2</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_62196_T2</span></div>
<div class="block"><p>IEC 62196 Type 2 "Mennekes".</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_62196_T2">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IEC_62196_T2_COMBO">
<h3>IEC_62196_T2_COMBO</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_62196_T2_COMBO</span></div>
<div class="block"><p>Combo Type 2 based, DC.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_62196_T2_COMBO">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IEC_62196_T3A">
<h3>IEC_62196_T3A</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_62196_T3A</span></div>
<div class="block"><p>IEC 62196 Type 3A.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_62196_T3A">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IEC_62196_T3C">
<h3>IEC_62196_T3C</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_62196_T3C</span></div>
<div class="block"><p>IEC 62196 Type 3C "Scame".</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_62196_T3C">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NEMA_5_20">
<h3>NEMA_5_20</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NEMA_5_20</span></div>
<div class="block"><p>NEMA 5-20, 3 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.NEMA_5_20">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NEMA_6_30">
<h3>NEMA_6_30</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NEMA_6_30</span></div>
<div class="block"><p>NEMA 6-30, 3 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.NEMA_6_30">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NEMA_6_50">
<h3>NEMA_6_50</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NEMA_6_50</span></div>
<div class="block"><p>NEMA 6-50, 3 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.NEMA_6_50">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NEMA_10_30">
<h3>NEMA_10_30</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NEMA_10_30</span></div>
<div class="block"><p>NEMA 10-30, 3 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.NEMA_10_30">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NEMA_10_50">
<h3>NEMA_10_50</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NEMA_10_50</span></div>
<div class="block"><p>NEMA 10-50, 3 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.NEMA_10_50">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NEMA_14_30">
<h3>NEMA_14_30</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NEMA_14_30</span></div>
<div class="block"><p>NEMA 14-30, 4 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.NEMA_14_30">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NEMA_14_50">
<h3>NEMA_14_50</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NEMA_14_50</span></div>
<div class="block"><p>NEMA 14-50, 4 pins.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.NEMA_14_50">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PANTOGRAPH_BOTTOM_UP">
<h3>PANTOGRAPH_BOTTOM_UP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PANTOGRAPH_BOTTOM_UP</span></div>
<div class="block"><p>On-board Bottom-up-Pantograph typically for bus charging.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.PANTOGRAPH_BOTTOM_UP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PANTOGRAPH_TOP_DOWN">
<h3>PANTOGRAPH_TOP_DOWN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PANTOGRAPH_TOP_DOWN</span></div>
<div class="block"><p>Top-down-Pantograph typically for bus charging.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.PANTOGRAPH_TOP_DOWN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TESLA_R">
<h3>TESLA_R</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TESLA_R</span></div>
<div class="block"><p>Tesla connector "Roadster"-type (round, 4 pin).</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.TESLA_R">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SAE_J3400">
<h3>SAE_J3400</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SAE_J3400</span></div>
<div class="block"><p>Tesla connector "Model-S"-type (oval, 5 pin), standardized as NACS SAE J3400.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.SAE_J3400">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MCS">
<h3>MCS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MCS</span></div>
<div class="block"><p>Megawatt Charging System (MCS) connector.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.ev.EVChargingConnectorType.MCS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>EVChargingConnectorType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">EVChargingConnectorType</span>()</div>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
</div>
</div>



</div>
`
}</HTMLBlock>
