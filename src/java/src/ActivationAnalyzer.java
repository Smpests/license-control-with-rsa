import com.sun.org.apache.xml.internal.security.utils.Base64;

import javax.crypto.Cipher;
import java.io.ByteArrayOutputStream;
import java.net.InetAddress;
import java.net.NetworkInterface;
import java.security.KeyFactory;
import java.security.PublicKey;
import java.security.spec.X509EncodedKeySpec;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * @author qingsong
 * created at 2019/8/19
 */
public class ActivationAnalyzer {
    private static final int MAX_DECRYPT_BLOCK = 256;
    /**
     * 解析激活码
     */
    public String analyzeActivateCode(String activateCode, String publicKey) throws Exception {
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.DECRYPT_MODE, getPublicKey(publicKey));
        byte[] code = Base64.decode(activateCode);
        int inputLen = code.length;
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        int offSet = 0;
        byte[] cache;
        int i = 0;
        // 对数据分段解密
        while (inputLen - offSet > 0) {
            if (inputLen - offSet > MAX_DECRYPT_BLOCK) {
                cache = cipher.doFinal(code, offSet, MAX_DECRYPT_BLOCK);
            } else {
                cache = cipher.doFinal(code, offSet, inputLen - offSet);
            }
            bos.write(cache, 0, cache.length);
            i++;
            offSet = i * MAX_DECRYPT_BLOCK;
        }
        bos.close();
        return Base64.encode(bos.toByteArray());
    }
    // Key String to PublicKey object
    private PublicKey getPublicKey(String publicKeyBase64) throws Exception {
        byte[] keyBytes;
        keyBytes = Base64.decode(publicKeyBase64);

        X509EncodedKeySpec keySpec = new X509EncodedKeySpec(keyBytes);
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        return keyFactory.generatePublic(keySpec);
    }
    /**
     * 获取机器MAC地址
     */
    private String getMAC(InetAddress address) throws Exception {
        //获取网卡，获取地址
        byte[] mac = NetworkInterface.getByInetAddress(address).getHardwareAddress();
        StringBuffer sb = new StringBuffer("");
        for(int i=0; i < mac.length; i++) {
            if(i!=0) {
                sb.append("-");
            }
            //字节转换为整数
            int temp = mac[i]&0xff;
            String str = Integer.toHexString(temp);
            if(str.length()==1) {
                sb.append("0"+str);
            }else {
                sb.append(str);
            }
        }
        return sb.toString().toUpperCase();
    }
    // 验证激活码
    public boolean validity(String activationCode, String publicKey) throws Exception {
    	String[] message = new String(Base64.decode(analyzeActivateCode(activationCode, publicKey)), "utf-8").split("&");
    	String MAC = message[0];
    	String dateStr = message[1];
        if (MAC.equals(getMAC(InetAddress.getLocalHost()))) {
            SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
            Date date = dateFormat.parse(dateStr);
            boolean result = date.after(new Date());
            if (result) {
                System.out.println("有效期内，请尽情使用!");
            } else {
                System.out.println("激活码已过期，请重新获取!");
            }
            return result;
        }
        System.out.println("MAC地址不匹配！请申请新的激活码。");
        return false;
    }
}
