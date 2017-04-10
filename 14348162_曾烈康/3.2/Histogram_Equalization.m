function Histogram_Equalization()
    close all 
    fi=imread('Fig3.08(a).jpg');
    figure,imshow(fi),title('原始图像')
    
    [m,n]=size(fi);
    Pr=zeros(1,256); 
    for k=0:255 
        Pr(k+1)=length(find(fi==k))/(m*n);  %统计灰度值为k的像素的出现概率
    end 
                   
    figure(1),bar(0:255,Pr,'k'),title('原始图像直方图')
    xlabel('灰度值'),ylabel('出现概率');     %打印原始图像直方图
    saveas(1,'oringin_hist.jpg');
    
    sumPr=zeros(1,256); 
    for i=1:256 
        for j=1:i 
            sumPr(i)=Pr(j)*255+sumPr(i);      %均衡化函数：对每个灰度i求和灰度0~i的概率
        end 
    end 
    
    figure(2),plot(0:255,sumPr,'k'),title('均衡化函数')
    xlabel('灰度值'),ylabel('出现概率');   %打印均衡化函数
    saveas(2,'eq_plot.jpg');
    
    newGray=round((sumPr)+0.5);       %对每个灰度的概率求对应的新的灰度值并四舍五入
    for i=1:256 
        Ps(i)=sum(Pr(newGray==i));        %ps(i)表示灰度为i的像素出现的概率
    end 
    
    figure(3),bar(0:255,Ps,'k'),title('均衡化后的直方图')
    xlabel('灰度值'),ylabel('出现概率');   %打印均衡化后的直方图
    saveas(3,'new_hist.jpg');
    
    fiEq=fi; 
    for i=0:255 
        fiEq(fi==i)=newGray(i+1);         %对fi中灰度为i的像素俊替换为newGray中的新灰度
    end 
    figure,imshow(fiEq),title('均衡化后图像');
    imwrite(fiEq,'Fig3.08(a)Eq.jpg'); 