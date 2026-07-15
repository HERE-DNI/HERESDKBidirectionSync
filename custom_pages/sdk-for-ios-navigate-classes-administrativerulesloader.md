---
title: "AdministrativeRulesLoader Class Reference"
slug: "sdk-for-ios-navigate-classes-administrativerulesloader"
---

# AdministrativeRulesLoader

<div class="declaration">

<div class="language">

``` highlight
public class AdministrativeRulesLoader
```

``` highlight
extension AdministrativeRulesLoader: NativeBase
```

``` highlight
extension AdministrativeRulesLoader: Hashable
```

</div>

</div>

Provides the protocol for the access to the administrative rules available for a country or a state in the local OCM map. Please be aware that the methods within this classload map data synchronously. In the event of absent data in the disk cache, the data will be retrieved from the remote server. To mitigate the potential freezing of the calling thread, it is advisable to proactively prefetch map data around the working area.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init () throws
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      init(sdkEngine: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( sdkEngine : SDKNativeEngine ) throws
  ```

  </pre>

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
  <td><code> </code><em><code>sdkEngine</code></em><code> </code></td>
  <td><div>
  <p>A SDKEngine instance.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      getStateCodes(countryCode: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Synchronously loads the list of state codes from a specified country for which administrative rules are availabe. These state codes can then be used to get specific administrative rules for a specified state using the

      get_administrative_rules()

  method. Returns a list with all the state codes available in the country. In case the country has no states, the list will be empty.
  </p>

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-mapdata#/s:7heresdk18MapDataLoaderErrora">`MapDataLoaderError`</a> Specifies reason, why the list of state codes was not returned.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getStateCodes ( countryCode : CountryCode ) throws -> [ String ]
  ```

  </pre>

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
  <td><code> </code><em><code>countryCode</code></em><code> </code></td>
  <td><div>
  <p>The country code for which the state codes are going to be retrieved.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The list of state codes present in the country for which administrative rules are available. Throws if it’s not possible to return the list of state codes.

  </div>

  </div>

  </div>

- <div>

      getAdministrativeRules(countryCode: stateCode: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Synchronously load the administrative rules for the specified country and state. **Note:** The `state_code` parameter can be set to `nil`. In this case, even if the country has multiple states, each with their own administrative rules, an <a href="sdk-for-ios-navigate-structs-administrativerules">`AdministrativeRules`</a> object will be returned, containing the administrative rules valid for the entire country. These rules can however be overwritten by the state rules when the driver is in that specific state, so it is recommended to always retrieve the rules for a specific state for higher accuracy. Returns an <a href="sdk-for-ios-navigate-structs-administrativerules">`AdministrativeRules`</a> object which contains the administrative rules for the specified country and state.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-mapdata#/s:7heresdk18MapDataLoaderErrora">`MapDataLoaderError`</a> Specifies reason, why the administrative rules were not retrieved.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getAdministrativeRules ( countryCode : CountryCode , stateCode : String ?) throws -> AdministrativeRules
  ```

  </pre>

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
  <td><code> </code><em><code>countryCode</code></em><code> </code></td>
  <td><div>
  <p>The country code for which the administrative rules will be retrieved.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>stateCode</code></em><code> </code></td>
  <td><div>
  <p>The state name for which the administrative rules will be received. It can be <code>nil</code>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Requested administrative rules for the country and the state specified.

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

