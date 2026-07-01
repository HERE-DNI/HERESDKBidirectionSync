---
title: "EVChargingConnectorType (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.ev](sdk-for-android-explore-com-here-sdk-ev-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.ev.EVChargingConnectorType

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">EVChargingConnectorType</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents the standardized type of the installed connector. Note: This
is a beta release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a
deprecation process.

</div>

</div>

<div class="section summary">

- <div id="field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Field</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#CHADEMO"
  class="member-name-link"><code>CHADEMO</code></a></td>
  <td><div class="block">
  The connector type is CHAdeMO, DC.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#CHAOJI"
  class="member-name-link"><code>CHAOJI</code></a></td>
  <td><div class="block">
  The ChaoJi connector.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#DOMESTIC_A"
  class="member-name-link"><code>DOMESTIC_A</code></a></td>
  <td><div class="block">
  Standard/Domestic household, type "A", NEMA 1-15, 2 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#DOMESTIC_B"
  class="member-name-link"><code>DOMESTIC_B</code></a></td>
  <td><div class="block">
  Standard/Domestic household, type "B", NEMA 5-15, 3 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#DOMESTIC_C"
  class="member-name-link"><code>DOMESTIC_C</code></a></td>
  <td><div class="block">
  Standard/Domestic household, type "C", CEE 7/17, 2 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#DOMESTIC_D"
  class="member-name-link"><code>DOMESTIC_D</code></a></td>
  <td><div class="block">
  Standard/Domestic household, type "D", 3 pin.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#DOMESTIC_E"
  class="member-name-link"><code>DOMESTIC_E</code></a></td>
  <td><div class="block">
  Standard/Domestic household, type "E", CEE 7/5 3 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#DOMESTIC_F"
  class="member-name-link"><code>DOMESTIC_F</code></a></td>
  <td><div class="block">
  Standard/Domestic household, type "F", CEE 7/4, Schuko, 3 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#DOMESTIC_G"
  class="member-name-link"><code>DOMESTIC_G</code></a></td>
  <td><div class="block">
  Standard/Domestic household, type "G", BS 1363, Commonwealth, 3 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#DOMESTIC_H"
  class="member-name-link"><code>DOMESTIC_H</code></a></td>
  <td><div class="block">
  Standard/Domestic household, type "H", SI-32, 3 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#DOMESTIC_I"
  class="member-name-link"><code>DOMESTIC_I</code></a></td>
  <td><div class="block">
  Standard/Domestic household, type "I", AS 3112, 3 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#DOMESTIC_J"
  class="member-name-link"><code>DOMESTIC_J</code></a></td>
  <td><div class="block">
  Standard/Domestic household, type "J", SEV 1011, 3 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#DOMESTIC_K"
  class="member-name-link"><code>DOMESTIC_K</code></a></td>
  <td><div class="block">
  Standard/Domestic household, type "K", DS 60884-2-D1, 3 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#DOMESTIC_L"
  class="member-name-link"><code>DOMESTIC_L</code></a></td>
  <td><div class="block">
  Standard/Domestic household, type "L", CEI 23-16-VII, 3 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#DOMESTIC_M"
  class="member-name-link"><code>DOMESTIC_M</code></a></td>
  <td><div class="block">
  Standard/Domestic household, type "M", BS 546, 3 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#DOMESTIC_N"
  class="member-name-link"><code>DOMESTIC_N</code></a></td>
  <td><div class="block">
  Standard/Domestic household, type "N", NBR 14136, 3 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#DOMESTIC_O"
  class="member-name-link"><code>DOMESTIC_O</code></a></td>
  <td><div class="block">
  Standard/Domestic household, type "O", TIS 166-2549, 3 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#GBT_AC"
  class="member-name-link"><code>GBT_AC</code></a></td>
  <td><div class="block">
  Guobiao GB/T 20234.2 AC socket/connector.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#GBT_DC"
  class="member-name-link"><code>GBT_DC</code></a></td>
  <td><div class="block">
  Guobiao GB/T 20234.3 DC connector.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#IEC_60309_2_SINGLE_16"
  class="member-name-link"><code>IEC_60309_2_SINGLE_16</code></a></td>
  <td><div class="block">
  IEC 60309-2 Industrial connector single phase 16 amperes (usually blue).
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#IEC_60309_2_THREE_16"
  class="member-name-link"><code>IEC_60309_2_THREE_16</code></a></td>
  <td><div class="block">
  IEC 60309-2 Industrial connector three phase 16 amperes (usually red).
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#IEC_60309_2_THREE_32"
  class="member-name-link"><code>IEC_60309_2_THREE_32</code></a></td>
  <td><div class="block">
  IEC 60309-2 Industrial connector three phase 32 amperes (usually red).
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#IEC_60309_2_THREE_64"
  class="member-name-link"><code>IEC_60309_2_THREE_64</code></a></td>
  <td><div class="block">
  IEC 60309-2 Industrial connector three phase 64 amperes (usually red).
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#IEC_62196_T1"
  class="member-name-link"><code>IEC_62196_T1</code></a></td>
  <td><div class="block">
  IEC 62196 Type 1 "SAE J1772".
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#IEC_62196_T1_COMBO"
  class="member-name-link"><code>IEC_62196_T1_COMBO</code></a></td>
  <td><div class="block">
  Combo Type 1 based, DC.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#IEC_62196_T2"
  class="member-name-link"><code>IEC_62196_T2</code></a></td>
  <td><div class="block">
  IEC 62196 Type 2 "Mennekes".
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#IEC_62196_T2_COMBO"
  class="member-name-link"><code>IEC_62196_T2_COMBO</code></a></td>
  <td><div class="block">
  Combo Type 2 based, DC.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#IEC_62196_T3A"
  class="member-name-link"><code>IEC_62196_T3A</code></a></td>
  <td><div class="block">
  IEC 62196 Type 3A.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#IEC_62196_T3C"
  class="member-name-link"><code>IEC_62196_T3C</code></a></td>
  <td><div class="block">
  IEC 62196 Type 3C "Scame".
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#MCS"
  class="member-name-link"><code>MCS</code></a></td>
  <td><div class="block">
  Megawatt Charging System (MCS) connector.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#NEMA_10_30"
  class="member-name-link"><code>NEMA_10_30</code></a></td>
  <td><div class="block">
  NEMA 10-30, 3 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#NEMA_10_50"
  class="member-name-link"><code>NEMA_10_50</code></a></td>
  <td><div class="block">
  NEMA 10-50, 3 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#NEMA_14_30"
  class="member-name-link"><code>NEMA_14_30</code></a></td>
  <td><div class="block">
  NEMA 14-30, 4 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#NEMA_14_50"
  class="member-name-link"><code>NEMA_14_50</code></a></td>
  <td><div class="block">
  NEMA 14-50, 4 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#NEMA_5_20"
  class="member-name-link"><code>NEMA_5_20</code></a></td>
  <td><div class="block">
  NEMA 5-20, 3 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#NEMA_6_30"
  class="member-name-link"><code>NEMA_6_30</code></a></td>
  <td><div class="block">
  NEMA 6-30, 3 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#NEMA_6_50"
  class="member-name-link"><code>NEMA_6_50</code></a></td>
  <td><div class="block">
  NEMA 6-50, 3 pins.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#PANTOGRAPH_BOTTOM_UP"
  class="member-name-link"><code>PANTOGRAPH_BOTTOM_UP</code></a></td>
  <td><div class="block">
  On-board Bottom-up-Pantograph typically for bus charging.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#PANTOGRAPH_TOP_DOWN"
  class="member-name-link"><code>PANTOGRAPH_TOP_DOWN</code></a></td>
  <td><div class="block">
  Top-down-Pantograph typically for bus charging.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#SAE_J3400"
  class="member-name-link"><code>SAE_J3400</code></a></td>
  <td><div class="block">
  Tesla connector "Model-S"-type (oval, 5 pin), standardized as NACS SAE
  J3400.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-ev-evchargingconnectortype#TESLA_R"
  class="member-name-link"><code>TESLA_R</code></a></td>
  <td><div class="block">
  Tesla connector "Roadster"-type (round, 4 pin).
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Constructor</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><pre><code>EVChargingConnectorType()</code></pre></td>
  <td> </td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="field-detail" class="section field-details">

  - <div id="CHADEMO" class="section detail">

    ### CHADEMO

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">CHADEMO</span>

    </div>

    <div class="block">

    The connector type is CHAdeMO, DC.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.CHADEMO)

    </div>

  - <div id="CHAOJI" class="section detail">

    ### CHAOJI

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">CHAOJI</span>

    </div>

    <div class="block">

    The ChaoJi connector. The new generation charging connector,
    harmonized between CHAdeMO and GB/T. DC.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.CHAOJI)

    </div>

  - <div id="DOMESTIC_A" class="section detail">

    ### DOMESTIC_A

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_A</span>

    </div>

    <div class="block">

    Standard/Domestic household, type "A", NEMA 1-15, 2 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_A)

    </div>

  - <div id="DOMESTIC_B" class="section detail">

    ### DOMESTIC_B

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_B</span>

    </div>

    <div class="block">

    Standard/Domestic household, type "B", NEMA 5-15, 3 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_B)

    </div>

  - <div id="DOMESTIC_C" class="section detail">

    ### DOMESTIC_C

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_C</span>

    </div>

    <div class="block">

    Standard/Domestic household, type "C", CEE 7/17, 2 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_C)

    </div>

  - <div id="DOMESTIC_D" class="section detail">

    ### DOMESTIC_D

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_D</span>

    </div>

    <div class="block">

    Standard/Domestic household, type "D", 3 pin.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_D)

    </div>

  - <div id="DOMESTIC_E" class="section detail">

    ### DOMESTIC_E

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_E</span>

    </div>

    <div class="block">

    Standard/Domestic household, type "E", CEE 7/5 3 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_E)

    </div>

  - <div id="DOMESTIC_F" class="section detail">

    ### DOMESTIC_F

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_F</span>

    </div>

    <div class="block">

    Standard/Domestic household, type "F", CEE 7/4, Schuko, 3 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_F)

    </div>

  - <div id="DOMESTIC_G" class="section detail">

    ### DOMESTIC_G

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_G</span>

    </div>

    <div class="block">

    Standard/Domestic household, type "G", BS 1363, Commonwealth, 3
    pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_G)

    </div>

  - <div id="DOMESTIC_H" class="section detail">

    ### DOMESTIC_H

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_H</span>

    </div>

    <div class="block">

    Standard/Domestic household, type "H", SI-32, 3 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_H)

    </div>

  - <div id="DOMESTIC_I" class="section detail">

    ### DOMESTIC_I

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_I</span>

    </div>

    <div class="block">

    Standard/Domestic household, type "I", AS 3112, 3 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_I)

    </div>

  - <div id="DOMESTIC_J" class="section detail">

    ### DOMESTIC_J

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_J</span>

    </div>

    <div class="block">

    Standard/Domestic household, type "J", SEV 1011, 3 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_J)

    </div>

  - <div id="DOMESTIC_K" class="section detail">

    ### DOMESTIC_K

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_K</span>

    </div>

    <div class="block">

    Standard/Domestic household, type "K", DS 60884-2-D1, 3 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_K)

    </div>

  - <div id="DOMESTIC_L" class="section detail">

    ### DOMESTIC_L

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_L</span>

    </div>

    <div class="block">

    Standard/Domestic household, type "L", CEI 23-16-VII, 3 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_L)

    </div>

  - <div id="DOMESTIC_M" class="section detail">

    ### DOMESTIC_M

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_M</span>

    </div>

    <div class="block">

    Standard/Domestic household, type "M", BS 546, 3 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_M)

    </div>

  - <div id="DOMESTIC_N" class="section detail">

    ### DOMESTIC_N

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_N</span>

    </div>

    <div class="block">

    Standard/Domestic household, type "N", NBR 14136, 3 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_N)

    </div>

  - <div id="DOMESTIC_O" class="section detail">

    ### DOMESTIC_O

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">DOMESTIC_O</span>

    </div>

    <div class="block">

    Standard/Domestic household, type "O", TIS 166-2549, 3 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.DOMESTIC_O)

    </div>

  - <div id="GBT_AC" class="section detail">

    ### GBT_AC

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">GBT_AC</span>

    </div>

    <div class="block">

    Guobiao GB/T 20234.2 AC socket/connector.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.GBT_AC)

    </div>

  - <div id="GBT_DC" class="section detail">

    ### GBT_DC

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">GBT_DC</span>

    </div>

    <div class="block">

    Guobiao GB/T 20234.3 DC connector.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.GBT_DC)

    </div>

  - <div id="IEC_60309_2_SINGLE_16" class="section detail">

    ### IEC_60309_2_SINGLE_16

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_60309_2_SINGLE_16</span>

    </div>

    <div class="block">

    IEC 60309-2 Industrial connector single phase 16 amperes (usually
    blue).

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_60309_2_SINGLE_16)

    </div>

  - <div id="IEC_60309_2_THREE_16" class="section detail">

    ### IEC_60309_2_THREE_16

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_60309_2_THREE_16</span>

    </div>

    <div class="block">

    IEC 60309-2 Industrial connector three phase 16 amperes (usually
    red).

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_60309_2_THREE_16)

    </div>

  - <div id="IEC_60309_2_THREE_32" class="section detail">

    ### IEC_60309_2_THREE_32

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_60309_2_THREE_32</span>

    </div>

    <div class="block">

    IEC 60309-2 Industrial connector three phase 32 amperes (usually
    red).

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_60309_2_THREE_32)

    </div>

  - <div id="IEC_60309_2_THREE_64" class="section detail">

    ### IEC_60309_2_THREE_64

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_60309_2_THREE_64</span>

    </div>

    <div class="block">

    IEC 60309-2 Industrial connector three phase 64 amperes (usually
    red).

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_60309_2_THREE_64)

    </div>

  - <div id="IEC_62196_T1" class="section detail">

    ### IEC_62196_T1

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_62196_T1</span>

    </div>

    <div class="block">

    IEC 62196 Type 1 "SAE J1772".

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_62196_T1)

    </div>

  - <div id="IEC_62196_T1_COMBO" class="section detail">

    ### IEC_62196_T1_COMBO

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_62196_T1_COMBO</span>

    </div>

    <div class="block">

    Combo Type 1 based, DC.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_62196_T1_COMBO)

    </div>

  - <div id="IEC_62196_T2" class="section detail">

    ### IEC_62196_T2

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_62196_T2</span>

    </div>

    <div class="block">

    IEC 62196 Type 2 "Mennekes".

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_62196_T2)

    </div>

  - <div id="IEC_62196_T2_COMBO" class="section detail">

    ### IEC_62196_T2_COMBO

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_62196_T2_COMBO</span>

    </div>

    <div class="block">

    Combo Type 2 based, DC.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_62196_T2_COMBO)

    </div>

  - <div id="IEC_62196_T3A" class="section detail">

    ### IEC_62196_T3A

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_62196_T3A</span>

    </div>

    <div class="block">

    IEC 62196 Type 3A.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_62196_T3A)

    </div>

  - <div id="IEC_62196_T3C" class="section detail">

    ### IEC_62196_T3C

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">IEC_62196_T3C</span>

    </div>

    <div class="block">

    IEC 62196 Type 3C "Scame".

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.IEC_62196_T3C)

    </div>

  - <div id="NEMA_5_20" class="section detail">

    ### NEMA_5_20

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">NEMA_5_20</span>

    </div>

    <div class="block">

    NEMA 5-20, 3 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.NEMA_5_20)

    </div>

  - <div id="NEMA_6_30" class="section detail">

    ### NEMA_6_30

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">NEMA_6_30</span>

    </div>

    <div class="block">

    NEMA 6-30, 3 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.NEMA_6_30)

    </div>

  - <div id="NEMA_6_50" class="section detail">

    ### NEMA_6_50

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">NEMA_6_50</span>

    </div>

    <div class="block">

    NEMA 6-50, 3 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.NEMA_6_50)

    </div>

  - <div id="NEMA_10_30" class="section detail">

    ### NEMA_10_30

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">NEMA_10_30</span>

    </div>

    <div class="block">

    NEMA 10-30, 3 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.NEMA_10_30)

    </div>

  - <div id="NEMA_10_50" class="section detail">

    ### NEMA_10_50

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">NEMA_10_50</span>

    </div>

    <div class="block">

    NEMA 10-50, 3 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.NEMA_10_50)

    </div>

  - <div id="NEMA_14_30" class="section detail">

    ### NEMA_14_30

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">NEMA_14_30</span>

    </div>

    <div class="block">

    NEMA 14-30, 4 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.NEMA_14_30)

    </div>

  - <div id="NEMA_14_50" class="section detail">

    ### NEMA_14_50

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">NEMA_14_50</span>

    </div>

    <div class="block">

    NEMA 14-50, 4 pins.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.NEMA_14_50)

    </div>

  - <div id="PANTOGRAPH_BOTTOM_UP" class="section detail">

    ### PANTOGRAPH_BOTTOM_UP

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">PANTOGRAPH_BOTTOM_UP</span>

    </div>

    <div class="block">

    On-board Bottom-up-Pantograph typically for bus charging.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.PANTOGRAPH_BOTTOM_UP)

    </div>

  - <div id="PANTOGRAPH_TOP_DOWN" class="section detail">

    ### PANTOGRAPH_TOP_DOWN

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">PANTOGRAPH_TOP_DOWN</span>

    </div>

    <div class="block">

    Top-down-Pantograph typically for bus charging.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.PANTOGRAPH_TOP_DOWN)

    </div>

  - <div id="TESLA_R" class="section detail">

    ### TESLA_R

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TESLA_R</span>

    </div>

    <div class="block">

    Tesla connector "Roadster"-type (round, 4 pin).

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.TESLA_R)

    </div>

  - <div id="SAE_J3400" class="section detail">

    ### SAE_J3400

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">SAE_J3400</span>

    </div>

    <div class="block">

    Tesla connector "Model-S"-type (oval, 5 pin), standardized as NACS
    SAE J3400.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.SAE_J3400)

    </div>

  - <div id="MCS" class="section detail">

    ### MCS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">MCS</span>

    </div>

    <div class="block">

    Megawatt Charging System (MCS) connector.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.ev.EVChargingConnectorType.MCS)

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### EVChargingConnectorType

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">EVChargingConnectorType</span>()

    </div>

    </div>

  </div>

</div>

