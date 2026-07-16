---
title: "SDKLogger Class Reference"
slug: "sdk-for-ios-explore-classes-sdklogger"
---

# SDKLogger

<div class="declaration">

<div class="language">

``` highlight
public class SDKLogger
```

``` highlight
extension SDKLogger: NativeBase
```

``` highlight
extension SDKLogger: Hashable
```

</div>

</div>

Logging interface for Android/iOS platforms. These logs are under management of <a href="sdk-for-ios-explore-classes-logcontrol">`LogControl`</a> and should be used instead of platform-specific logging functions.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9SDKLoggerC3log5level3tag7messageyAA8LogLevelO_S2StFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-log-level-tag-message" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdklogger#sdk-for-ios-explore-s-7heresdk9SDKLoggerC3log5level3tag7messageyAA8LogLevelO_S2StFZ" class="token"><code>log(level:</code><wbr></wbr><code>tag:</code><wbr></wbr><code>message:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func log(level: LogLevel, tag: String, message: String)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-loglevel">LogLevel</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>level</code></em><code> </code></td>
  <td><div>
  <p>The severity of the log message.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>tag</code></em><code> </code></td>
  <td><div>
  <p>The log tag.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>message</code></em><code> </code></td>
  <td><div>
  <p>The log message.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9SDKLoggerC4info3tag7messageySS_SStFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-info-tag-message" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdklogger#sdk-for-ios-explore-s-7heresdk9SDKLoggerC4info3tag7messageySS_SStFZ" class="token"><code>info(tag:</code><wbr></wbr><code>message:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  convenient function to print a message with log level INFO and tag.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func info(tag: String, message: String)
  ```

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>tag</code></em><code> </code></td>
  <td><div>
  <p>The log tag.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>message</code></em><code> </code></td>
  <td><div>
  <p>The log message.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9SDKLoggerC4warn3tag7messageySS_SStFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-warn-tag-message" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdklogger#sdk-for-ios-explore-s-7heresdk9SDKLoggerC4warn3tag7messageySS_SStFZ" class="token"><code>warn(tag:</code><wbr></wbr><code>message:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  convenient function to print a message with log level WARNING and tag.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func warn(tag: String, message: String)
  ```

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>tag</code></em><code> </code></td>
  <td><div>
  <p>The log tag.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>message</code></em><code> </code></td>
  <td><div>
  <p>The log message.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9SDKLoggerC5error3tag7messageySS_SStFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-error-tag-message" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdklogger#sdk-for-ios-explore-s-7heresdk9SDKLoggerC5error3tag7messageySS_SStFZ" class="token"><code>error(tag:</code><wbr></wbr><code>message:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  convenient function to print a message with log level ERROR and tag.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func error(tag: String, message: String)
  ```

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>tag</code></em><code> </code></td>
  <td><div>
  <p>The log tag.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>message</code></em><code> </code></td>
  <td><div>
  <p>The log message.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9SDKLoggerC5fatal3tag7messageySS_SStFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-fatal-tag-message" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-sdklogger#sdk-for-ios-explore-s-7heresdk9SDKLoggerC5fatal3tag7messageySS_SStFZ" class="token"><code>fatal(tag:</code><wbr></wbr><code>message:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  convenient function to print a message with log level FATAL and tag.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func fatal(tag: String, message: String)
  ```

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>tag</code></em><code> </code></td>
  <td><div>
  <p>The log tag.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>message</code></em><code> </code></td>
  <td><div>
  <p>The log message.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

