import com.sun.org.apache.xml.internal.security.utils.Base64;

/**
 * @author qingsong
 * created at 2019/8/20
 */
public class Main {
    public static void main(String[] args) throws Exception {
        String activationCode = "";
        String publicKeyBase64 = "";
        ActivationAnalyzer analyzer = new ActivationAnalyzer();
        // 验证Mac和有效期
        if (analyzer.validity(activationCode, publicKeyBase64)) {
            // 验证成功执行的代码
            System.out.println(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>使用中");
        } else {
            // 验证失败要执行的代码
            System.out.println(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>不让使用");
        }
    }
}
